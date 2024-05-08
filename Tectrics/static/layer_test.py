import json

# JSON 파일을 읽어옵니다.
with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items copy.json', 'r') as file:
    data = json.load(file)

    color_map = {
        1: "#FF9999",  # 레이어 1에 대한 색상 (빨간색)
        2: "#99FF99",  # 레이어 2에 대한 색상 (녹색)
        3: "#9999FF"   # 레이어 3에 대한 색상 (파란색)
    }
    for box in data:
        # center_x = box['positionX'] + box['width'] / 2  # 중심점 X 좌표 계산
        if 0 <= box['positionX'] < 500:
            box['color'] = color_map[1]
        elif 500 <= box['positionX'] < 1000:
            box['color'] = color_map[2]
        elif 1000 <= box['positionX'] < 2700:
            box['color'] = color_map[3] 
        

# JSON 파일로 데이터 저장
def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# 변경된 데이터를 파일에 씁니다.
with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items copy.json', 'w') as file:
    json.dump(data, file, indent=4)
