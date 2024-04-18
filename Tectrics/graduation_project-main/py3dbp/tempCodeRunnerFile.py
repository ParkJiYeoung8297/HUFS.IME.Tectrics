    items_data = []

            for bin in self.bins:
            # 각 아이템의 정보를 딕셔너리 형태로 변환하여 리스트에 추가
                for item in bin.items:
                                item_data = {
                    "partno": item.partno,
                    "width": item.width,
                    "height": item.height,
                    "depth": item.depth,
                    "position": {
                        "x": item.position[0],
                        "y": item.position[1],
                        "z": item.position[2]
                    },
                    "color": item.color,
                }
                                items_data.append(item_data)

        # 리스트를 JSON 파일로 저장
                with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items.json', 'w') as json_file:
                    json.dump(items_data, json_file, indent=4)