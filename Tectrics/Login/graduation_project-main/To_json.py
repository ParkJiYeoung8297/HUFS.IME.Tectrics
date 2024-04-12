import json

# 예를 들어, 여러 Bin 객체가 리스트에 저장되어 있다고 가정
#bins = [bin1, bin2, bin3]  # Bin 객체들의 리스트

# Bin 객체들을 딕셔너리 리스트로 변환
#bins_dict = [bin_to_dict(bin) for bin in bins]

# 딕셔너리를 JSON 문자열로 변환
bins_json = json.dumps(bins_dict, indent=4)

# JSON 문자열을 파일에 쓰기
with open('bins_data.json', 'w') as file:
    file.write(bins_json)
