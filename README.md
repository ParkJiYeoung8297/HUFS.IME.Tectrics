자세한 정보는 노션에 있습니다 : https://iodized-chartreuse-9ca.notion.site/tectrics

### 1. 프로젝트 동기 및 목표

1)프로젝트 배경

택배업에 관련된 근로자 수도 지속적으로 증가하며, 택배 배송을 책임지는 택배기사들의 업무상 어려움도 증가하고 있다.
<img width="725" alt="image" src="https://github.com/user-attachments/assets/e900c5d2-aef3-493d-90d9-0a0726d22220" />

또한 물류 산업의 성장과 더불어 택배의 물동량이 증가함에 따라 신입 배송기사 및 일일 배송 기사의 수가 증가 하고 있다. 가장 대표적인 배송 알바 앱인 “쿠팡 플렉스”의 이용자수는 출시했던 2019 년 212 명, 2020 년 5481 명으로 매년 가파르게 증가하고 있다. 이에 따라 배송에 익숙치 않은 많은 초보 기사들이 배송 경로 설정과 적재에 대한 어려움을 겪고 있다.

2)프로젝트 목표 

본 프로젝트에서는 **배송 순서를 고려한 탑차 택배 적재 시스템을 구현**하여 배송 네비게이션 및 적재 방법 가이드 기능을 제공한다. 초보 배송기사는 우리의 서비스를 사용함으로써 **숙련자 만큼의 효율을 낼 수 있도록 하는 것이 프로젝트 목표**이다.

3)역할 분담

역할은 경로 문제와 적재 방법 문제로 나누었고, 그 중 나는 경로 문제를  맡아 프로젝트를 진행하였다.

또한 깃을 이용한 프로젝트 코드 관리와 웹&앱 개발 전반에 관해서는 대부분 맡아 진행하였다.

### 2. 프로젝트 진행

1)데이터

a. 택배 데이터 : 부피는 우체국 소포상자 규격별 판매 현황 데이터를 참고해 생성한다. 1 호 박스는 부피가
작아 행낭박스에 따로 적재한다고 가정하고 2, 2-1, 3, 4, 5 호 박스를 판매비율에 맞게 생성하여 활용한다.

b. 배송 목적지에 대한 데이터는 좌표로 생성하면 건물이 아닌 장소에도 배송 목적지로 뜰 수 있기 때문에 도로명 주소를 랜덤으로 추출하여 생성한다. 현재 외대로 주소 400 개, 태전동 주소 2000 개 두 가지 주소 데이터를 생성하였다.

2)프로세스

<img width="478" alt="image" src="https://github.com/user-attachments/assets/b0f2b38c-e6ae-4a50-af01-258019148fbc" />

1. 배송기사별 데이터가 its 장치로 인해 자동으로 DB에 들어간다.

2. 이를 바탕으로 도로명 주소 기준 경로를 설정하고 클러스터링하여 레이어별 택배를 할당한다.

3. 택배기사가 모바일 앱으로 바코드를 찍으면 해당 박스에 대한 정보를 재공한다.


3)경로 설정

a. api 경로 설정의 문제점

초반에는 tmap api를 받아와서 경로를 설정하려고 했다. 하지만 중앙선을 넘나드는 비효율적인 경로 문제가 발생하였다. 다익스트라, A* 알고리즘과 같이 다른 경로 알고리즘을 고려하였으나, 문제가 해결되지 않았다. 경기도권에 도로명 주소는 특정한 규칙에 의해 숫자가 부여된다는 것을 발견했고, 이를 활용하여 알고리즘을 개발하였다.

<img width="643" alt="image" src="https://github.com/user-attachments/assets/61c5f2fd-5a1e-4e5e-bb0f-0a706a463117" />

b. 도로명 주소를 활용한 알고리즘

DFS를 응용하여, 노드가 있으면 해당 노드에 사이클은 전부 돌고 복귀하는 알고리즘이다.

<img width="645" alt="image" src="https://github.com/user-attachments/assets/b2829e72-378b-4666-ba5e-919a5c07ab34" />

c. 알고리즘 코드
사용한 주요 함수들은 다음과 같다.
# 사이클 생성

```python

def makeCycles(df,start):
    A=df
    A=A.sort_values("도로번호")

    from collections import deque

    A_0=deque()
    A_1=deque()
    for i in range(len(A)):
        if A["도로번호"].iloc[i]%2==0:     #짝수
            A_0.append(A["도로번호"].iloc[i])
        else:                           #홀수
            A_1.append(A["도로번호"].iloc[i])

    # start를 조절하면 됨
    #start=2592
    if A_0:  # A_0이 비어 있지 않으면
        start = A_0[0]
    elif A_1:  # A_1이 비어 있지 않으면
        start = A_1[0]

    A_cycles=deque()

    if A_0:  # A_0이 None이 아닌지 확인  
        print("낮 -> 높")
        if A_1:  # A_1이 비어 있지 않으면 reverse 실행
            A_1.reverse()
        A_0.extend(A_1)
        A_cycles = A_0  
        
    else:
        if A_1:  # A_1이 비어 있지 않으면
            A_cycles = A_1
            A_cycles.reverse()

```


# cycle 들을 연결하는 점 찾기

```python

def connect_node(df,dq):
    start=0
    index_value=0
    min_value=100000000

    for i in dq:
        sv=df[i].sort_values()
        for j in range(1,len(sv)):
            if (sv.index[j] not in dq):
                if (sv.loc[sv.index[j]]<=min_value):
                    start=i
                    min_value=sv.loc[sv.index[j]]  #걸린시간
                    index_value=sv.index[j]   # index
    result=[start,index_value,min_value]
    return result

```


# 사이클 돌아서 경로 추가하는 코드


```python

def cycle_route(start,df,dq,visit):
    node = start
    
    route = []

    if node in dq:
        if dq[0] != node:  # 시작점에 cycle 다시 짜기
            dq=makeCycles(df,node)
            cycle=makeCycles(dq,dq.loc[dq['index'] == node, '도로번호'].values[0])
            dq=deque(cycle["index"])


        for i in range(len(dq)):
            current_node = dq[0]
            route.append(current_node)  # 다음 노드 경로에 추가
            visit[current_node - 1] = 1  # 방문했다고 표시 (인덱스를 맞추기 위해 -1 사용)
            dq.append(dq.popleft())

    print("Route:", route)
    print("Visit:", visit)
    return route

```
    
# 가장 거리가 짧은 인덱스 구하기

```python

def findShortestNode(df_duration,node,Route):
    
    first_column = df_duration.iloc[node,:]
    min_index = first_column.nsmallest(2).idxmax()

    Route=deque(Route)
    for i in range(len(Route)):
        a=Route.popleft()
        if a==min_index:
            Route.appendleft(a)
            break
        else:
            Route.append(a)

    Route=list(Route)
    return Route

Route=findShortestNode(df_duration,0,Route)

```

d. 알고리즘으로 배송 순서 반환

<img width="716" alt="image" src="https://github.com/user-attachments/assets/77ee25a8-b35a-4980-a850-78a5538b77f5" />

사이클이 연결되어 하나의 큰 사이클로 통합되었다.

e. 클러스터링

이제 레이어 할당을 위해 클러스터링 필요하다. 

**투 포인터 방식을** 이용해 좌표 데이터를 클러스터링하고 Folium을 사용해 지도에 시각화하였다.

```python
import numpy as np
import folium

# 예제 배송 좌표 생성 (순서가 정해진 상태)
coordinates = np.array(gogo)

# 클러스터 수
num_clusters = 6

# 각 클러스터의 최대 크기
max_cluster_size = len(coordinates) // num_clusters + 1

# 투 포인터를 사용한 클러스터링
clusters = []
current_cluster = []

for point in coordinates:
    current_cluster.append(point)
    if len(current_cluster) == max_cluster_size:
        clusters.append(current_cluster)
        current_cluster = []

# 마지막 클러스터가 비어 있지 않으면 추가
if current_cluster:
    clusters.append(current_cluster)

# Folium 지도 생성
m = folium.Map(location=[37.3514335, 127.2474806], zoom_start=13)

# 클러스터링 결과 지도에 표시
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i, cluster in enumerate(clusters):
    for j, point in enumerate(cluster):
        folium.CircleMarker(
            location=(point[0], point[1]),
            radius=5,
            color=colors[i % len(colors)],
            fill=True,
            fill_color=colors[i % len(colors)]
        ).add_to(m)
        folium.Marker(
            location=(point[0], point[1]),
            icon=folium.DivIcon(html=f'<div style="font-size: 12pt; color : black">{j}</div>')
        ).add_to(m)
    
    # 클러스터 내 경로 그리기
    folium.PolyLine(cluster, color=colors[i % len(colors)], weight=2.5, opacity=1).add_to(m)

# 지도 저장 및 표시
m.save("map.html")
m

```

결과적으로는 아래와 같이 레이어가 잘 할당된것을 확인할 수 있다.

[결과]

<img width="224" alt="image" src="https://github.com/user-attachments/assets/d985262d-6631-4463-bcf1-d6f49c91798a" />


4) 알고리즘 성능

성능이 향상됐는지 확인하기 위해 tmap api를 호출하였다.

<aside>

경유지 순서 최적화 : 배송 순서와 경로를 제공하는 Tmap API
다중 경유지 안내 : 사용자가 입력한 경유지 순서대로 경로를 제공하는 Tmap API

</aside>


<img width="1387" alt="image" src="https://github.com/user-attachments/assets/09e22e8a-d4d5-4dd7-b0aa-a3d360157e86" />


도로명 주소 알고리즘 변경 이후 총 거리 39.9km -> 32.6km , 총 시간 121분 -> 103분으로 단축되었다.

### 3. 웹&앱 개발

1)DB 설계

개발에 들어가기 전 DB에 저장할 데이터 간의 의존성을 고려하였다.

<img width="726" alt="image" src="https://github.com/user-attachments/assets/c0a1c211-30e1-4d09-8279-fa819c3f98a1" />

2)장고와 플러터 기능 구현

<img width="723" alt="image" src="https://github.com/user-attachments/assets/7fe22dac-4719-4466-b9e7-0b66534fe680" />


기능은 장고에서 모두 만들고 api로 통신하여 모바일 앱으로도 사용할 수 있게 하였다.

3)모바일 시연

원래는 배포를 해야하는데 배포 없이도 모바일 폰에서 실행 시킬 수 있는 방법을 찾아서 배포없이 진행하였다.

 이때 유선으로 잭 연결하는 방법과 무선 연결 방법이 있었는데, 우리는 실험을 해야 하기 때문에 무선으로 연결하는 방법을 선택했다. (노션 개발 일지 [실제 모바일 기기 연결] 참고)

<img width="719" alt="image" src="https://github.com/user-attachments/assets/19d6dbe0-df27-441a-a31e-9565d72ccd4b" />

### 4. 시연 영상

노션 참고 : https://iodized-chartreuse-9ca.notion.site/tectrics
