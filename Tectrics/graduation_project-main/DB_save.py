# Python 코드에서 JSON 파일 읽기
import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

json_data = read_json_file('packed_items_layer.json')

# Python 코드에서 JSON 데이터를 Django 모델로 변환하고 저장하기
from .models import Load

def save_to_database(json_data):
    for item in json_data:
        obj = Load(
            field1=item['field1'],
            field2=item['field2'],
            # 필요한 경우 다른 필드들도 여기에 추가합니다.
        )
        obj.save()

# 위에서 읽은 JSON 데이터를 데이터베이스에 저장합니다.
save_to_database(json_data)
