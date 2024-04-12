from py3dbp import Packer, Bin, Item, Painter
import time
start = time.time()

'''

This example can be used to test large batch calculation time and binding functions.

'''

# init packing function
packer = Packer()

# Evergreen Real Container (20ft Steel Dry Cargo Container)

box = Bin('example', (610, 244, 259), 100, 0, 0)

packer.addBin(box)

# dyson DC34 (20.5 * 11.5 * 32.2 ,1.33kg)
# 64 pcs per case ,  82 * 46 * 170 (85.12)
for i in range(10): 
    packer.addItem(Item(
        partno='Dyson DC34 Animal{}'.format(str(i+1)),
        name='Dyson', 
        typeof='cube',
        WHD=(188, 28, 58), 
        weight=1,
        level=1,
        loadbear=1000,
        updown=True,
        color='yellow')
    )
# washing machine (85 * 60 *60 ,10 kG)
# 1 pcs per case, 85 * 60 *60 (10)
for i in range(36):
    packer.addItem(Item(
        partno='wash{}'.format(str(i+1)),
        name='wash',
        typeof='cube',
        WHD=(61, 9, 79), 
        weight=1,
        level=2,
        loadbear=1000,
        updown=True,
        color='brown'
    ))

# 42U standard cabinet (60 * 80 * 200 , 80 kg)
# one per box, 60 * 80 * 200 (80)
for i in range(14):
    packer.addItem(Item(
        partno='Cabinet{}'.format(str(i+1)),
        name='cabint',
        typeof='cube',
        WHD=(260, 39, 80), 
        weight=1,
        level=3,
        loadbear=1000,
        updown=True,
        color='red')
    )

# Server (70 * 100 * 30 , 20 kg) 
# one per box , 70 * 100 * 30 (20)
for i in range(5):
    packer.addItem(Item(
        partno='Server{}'.format(str(i+1)),
        name='server',
        typeof='cube',
        WHD=(145, 80, 96), 
        weight=1,
        level=4,
        loadbear=1000,
        updown=True,
        color='blue')
    )


# calculate packing
packer.pack(
    bigger_first=True,
    distribute_items=False,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.75,

    
)

# print result
for box in packer.bins:

    volume = box.width * box.height * box.depth
    print(":::::::::::", box.string())

    print("FITTED ITEMS:")
    volume_t = 0
    volume_f = 0
    unfitted_name = ''

    # '''
    for item in box.items:
        print("partno : ",item.partno)
        print("type : ",item.name)
        print("color : ",item.color)
        print("position : ",item.position)
        print("rotation type : ",item.rotation_type)
        print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
        print("volume : ",float(item.width) * float(item.height) * float(item.depth))
        print("weight : ",float(item.weight))
        volume_t += float(item.width) * float(item.height) * float(item.depth)
        print("***************************************************")
    print("***************************************************")
    # '''
    print("UNFITTED ITEMS:")
    for item in box.unfitted_items:
        print("partno : ",item.partno)
        print("type : ",item.name)
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
    print("gravity distribution : ",box.gravity)
    # '''
    stop = time.time()
    print('used time : ',stop - start)

    # draw results
    painter = Painter(box)
    fig = painter.plotBoxAndItems(
        title=box.partno,
        alpha=0.9,
        write_num=False,
        fontsize=6
    )
fig.show()