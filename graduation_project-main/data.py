import sqlite3
import json
import os

# SQLite 데이터베이스 파일 경로
database_path = '/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/db.sqlite3'

# 데이터베이스에 연결
conn = sqlite3.connect(database_path)

# 커서 생성
cursor = conn.cursor()

# SQL 쿼리 실행 (예: 테이블에서 모든 데이터 선택)
query = "SELECT id, box_code, width, height, depth From Order_boxdata"
cursor.execute(query)

# 결과 조회
rows = cursor.fetchall()


data = []
for row in rows:
    record = dict(zip([column[0] for column in cursor.description], row))
    # dimension 튜플 생성
    dimension = (record['width'], record['height'], record['depth'])
    # dimension을 데이터에 추가하고, 개별 length, width, height 삭제
    record['dimension'] = dimension
    del record['width'], record['height'], record['depth']
    data.append(record)
    
# data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

home_directory = os.path.expanduser('~')
file_path = os.path.join(home_directory,'graduation_project-main' 'output.json')
# JSON 파일로 저장
with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
# 연결 종료
conn.close()
