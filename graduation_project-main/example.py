import json
import random
from py3dbp import Packer, Bin, Item
import time

start = time.time()

def generate_random_color():
    """ RGB 형식의 랜덤 색상 생성 """
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

packer = Packer()

box = Bin('example', (16000, 18000, 20000), 500, 0, 0)

packer.addBin(box)

with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/output.json', 'r') as json_file:
    data = json.load(json_file)

# JSON 데이터에서 컨테이너 정보 읽기 및 추가
# for container_data in data['containers']:
#     name = container_data['name']
#     dimensions = tuple(container_data['dimensions'])
#     max_load = container_data['max_load']
#     packer.addBin(Bin(name, dimensions, max_load, 0, 0))

# JSON 데이터에서 아이템 정보 읽기 및 추가
for item_data in data:
    id = item_data['id']
    code= item_data['box_code']
    dimensions = tuple(item_data['dimension'])
    # weight = item_data['weight']
    # color = item_data['color']
    color = generate_random_color()
    print(data)
    #print(dimensions)
    packer.addItem(Item(id, code, 'cube', dimensions, 1, 1, 100, True, color))

# 패킹 실행
packer.pack(
    bigger_first=False,
    distribute_items=True,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.9,
)


# 결과 출력 (예시)
# ... [이전 코드 부분]

# 결과 출력 (예시)
for bin in packer.bins:
    print("===== {} =====".format(bin.partno))  # 'name' 대신 'partno' 사용
    for item in bin.items:
        print("Item: {}, width: {}, height:{},depth:{}, PositionX: {}, PositionY: {}, PositionZ: {}, Color{}".format(item.partno, item.width, item.height, item.depth, item.position[0], item.position[1], item.position[2], item.color))

