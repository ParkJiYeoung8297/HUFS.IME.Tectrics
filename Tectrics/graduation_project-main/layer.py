import json

def load_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

    # JSON 데이터를 여기에 붙여넣기
def update_box_layers(data):
  
    color_map = {
        1: "#FF0000",  # 레이어 1에 대한 색상 (빨간색)
        2: "#00FF00",  # 레이어 2에 대한 색상 (녹색)
        3: "#0000FF"   # 레이어 3에 대한 색상 (파란색)
    }
    for box in data:
        # center_x = box['positionX'] + box['width'] / 2  # 중심점 X 좌표 계산
        if 0 <= box['positionX'] <= 900:
            box['layer'] = 1
        elif 900 <= box['positionX'] <= 1800:
            box['layer'] = 2
        elif 1800 <= box['positionX'] < 2700:
            box['layer'] = 3
        box['color'] = color_map[box['layer']]

# JSON 파일로 데이터 저장
def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# 실행
original_file_path = '/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items.json'
new_file_path = '/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/graduation_project-main/packed_items_layer.json'
data = load_json_file(original_file_path)
update_box_layers(data)
save_to_json(data, new_file_path)

print("Updated layer information has been saved to the file.")

# 각 레이어 별로 박스를 분류하는 함수
# def classify_boxes_by_layers(data):
#     layer1 = []  # 0 ~ 900
#     layer2 = []  # 900 ~ 1800
#     layer3 = []  # 1800 ~ 2700

#     for box in data:
#         center_x = box['positionX'] + box['width'] / 2  # 중심점 X 좌표 계산

#         if 0 <= center_x < 900:
#             layer1.append(box)
#         elif 900 <= center_x < 1800:
#             layer2.append(box)
#         elif 1800 <= center_x < 2700:
#             layer3.append(box)

#     return layer1, layer2, layer3

# # 함수 실행
# layer1, layer2, layer3 = classify_boxes_by_layers(data)
# for box in layer2:
#   print(box['id'])
  
  

# 결과 출력
# print("Layer 1:", json.dumps(layer1, indent=4))
# print("Layer 2:", json.dumps(layer2, indent=4))
# print("Layer 3:", json.dumps(layer3, indent=4))
