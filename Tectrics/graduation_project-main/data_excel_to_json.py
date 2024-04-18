import pandas as pd
import json

# 엑셀 파일 경로
file_path = '/Users/hwang-yechan/HUFS.IME.Tectrics/delivery_list_v4.xlsx'

# 엑셀 파일 읽기
# 이 예제에서는 첫 번째 시트를 읽습니다. 필요에 따라 'sheet_name' 매개변수를 조정할 수 있습니다.
df = pd.read_excel(file_path, engine='openpyxl')

# 데이터 프레임을 JSON 형식으로 변환
# 'orient' 매개변수는 원하는 JSON 구조에 따라 조정할 수 있습니다. 
# 'records'는 각 행을 별도의 JSON 객체로 변환합니다.
data = []
for index, row in df.iterrows():
       # 'dimension' 키를 사용하여 길이, 너비, 높이를 튜플로 저장
    dimension = (row['length'], row['width'], row['height'])
    record = {
        'id': row['id'],
        'box_code': row['box_code'],
        'dimension': dimension
    }
    data.append(record)
    
output_json_path = 'output_data_v2.json'  # 파일 경로를 정확하게 수정
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"JSON 파일이 '{output_json_path}'에 저장되었습니다.")