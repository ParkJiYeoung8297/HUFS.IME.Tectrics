import sqlite3

import json

data = sqlite3.connect('db.sqlite3')
cur = data.cursor()


loaddata = json.load(open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/static/packed_items.json'))


# cur.execute("CREATE TABLE IF NOT EXISTS Load_loadedboxdata(id INTEGER PRIMARY KEY, userId text, title text, body text )")

myData =[]
# print(loaddata)
for data_dict in loaddata:

    # print(data_dict)
    # print(data_dict.keys())
    t = (data_dict['box_code'], data_dict['width'], data_dict['height'], data_dict['depth'], data_dict['volume'], data_dict['layer'], data_dict['deliverySequence'], data_dict['loadSequence'], data_dict['positionX'], data_dict['positionY'], data_dict['positionZ'], data_dict['color'])
    myData.append(t)
    
cur.executemany("INSERT INTO Load_loadedboxdata(box_code, width, height, depth, volume, layer, deliverySequence, loadSequence, positionX, positionY, positionZ, color) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", myData)

data.commit()

data.close()