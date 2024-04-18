import json
import random
from py3dbp import Packer, Bin, Item, Painter
import time

start = time.time()

def generate_random_color():
    """ RGB 형식의 랜덤 색상 생성 """
    return "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

packer = Packer()

box = Bin('example', (2700, 1600, 1600), 500, 0, 0)

packer.addBin(box)

with open('/Users/hwang-yechan/HUFS.IME.Tectrics/Tectrics/output1.json', 'r') as json_file:
    data = json.load(json_file)
    #print(data)
# print()


for item_data in data:
    # print(item_data)
    id = item_data['id']
    code= item_data['box_code']
    level = item_data['sequence']
    dimensions = tuple(item_data['dimension'])
    
    # color = item_data['color']
    color = generate_random_color()
    
   
    packer.addItem(Item(id, code, 'cube', dimensions, 1, level, 100, True, color))
print('wait')
# 패킹 실행
packer.pack(
    bigger_first=True,
    distribute_items=True,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.7,
)


# 결과 출력 (예시)
# ... [이전 코드 부분]

# 결과 출력 (예시)
for bin in packer.bins:
    print("===== {} =====".format(bin.partno))  # 'name' 대신 'partno' 사용
    for item in bin.items:
        print("Item: {}, width: {}, height:{},depth:{},PositionX: {}, PositionY: {}, PositionZ: {},Dsequence{}, Color{}".format(item.partno, item.width, item.height, item.depth, item.position[0], item.position[1], item.position[2], item.level, item.color))

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# def plot_container_combined(ax, container1, container2, offset_x=5, container1_title="Container 1", container2_title="Container 2", container1_color='blue', container2_color='green'):
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     for item in container1.items:
#         width, depth, height = item.getDimension()
#         x, y, z = item.position
#         ax.bar3d(x, y, z, width, depth, height, color=container1_color, alpha=0.5,edgecolor='k')

#     for item in container2.items:
#         width, depth, height = item.getDimension()
#         x, y, z = item.position
#         ax.bar3d(x + offset_x, y, z, width, depth, height, color=container2_color, alpha=0.5,edgecolor='k')

# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_subplot(111, projection='3d')


plt.show()

b = packer.bins[0]
volume = b.width * b.height * b.depth
print(":::::::::::", b.string())

print("FITTED ITEMS:")
volume_t = 0
volume_f = 0
unfitted_name = ''
for item in b.items:
    print("partno : ",item.partno)
    print("color : ",item.color)
    print("position : ",item.position)
    print("rotation type : ",item.rotation_type)
    print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
    print("volume : ",float(item.width) * float(item.height) * float(item.depth))
    print("weight : ",float(item.weight))
    print("level : ",item.level)    
    volume_t += float(item.width) * float(item.height) * float(item.depth)
    print("***************************************************")
print("***************************************************")
print("UNFITTED ITEMS:")
for item in b.unfitted_items:
    print("partno : ",item.partno)
    print("color : ",item.color)
    print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
    print("volume : ",float(item.width) * float(item.height) * float(item.depth))
    print("weight : ",float(item.weight))
    volume_f += float(item.width) * float(item.height) * float(item.depth)
    unfitted_name += '{},'.format(item.partno)
    print("***************************************************")
print("***************************************************")
print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
print('residual volumn : ', float(volume) - volume_t )
print('unpack item : ',unfitted_name)
print('unpack item volumn : ',volume_f)
print("gravity distribution : ",b.gravity)
stop = time.time()
print('used time : ',stop - start)

# draw results
painter = Painter(b)
fig = painter.plotBoxAndItems(
    title=b.partno,
    alpha=0.9,
    write_num=False,
    fontsize=10
)
fig.show()
#print(item1.position, item1.width, item1.depth, item1.height)