from py3dbp import Packer, Bin, Item, Painter
import time
start = time.time()

packer = Packer()
box = Bin('example1', (10, 4, 20), 70.0, 0, 0)

packer.addBin(box)
packer.addItem(Item('1', 'test','cube',(2, 2, 4), 1,1,100,True,'red'))
packer.addItem(Item('2', 'test','cube',(2, 2, 4), 1,1,100,True,'red'))
packer.addItem(Item('3', 'test','cube',(2, 2, 4), 1,1,100,True,'red'))
packer.addItem(Item('4', 'test','cube',(2, 2, 4), 1,1,100,True,'yellow'))
packer.addItem(Item('5', 'test','cube',(2, 2, 4), 1,1,100,True,'yellow'))
packer.addItem(Item('6', 'test','cube',(2, 2, 4), 1,1,100,True,'yellow'))
packer.addItem(Item('7', 'test','cube',(2, 2, 4), 1,1,100,True,'yellow'))
packer.addItem(Item('8', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('9', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('10', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('11', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('12', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('13', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('14', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('15', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('16', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))
packer.addItem(Item('17', 'test','cube',(4, 4, 2), 1,1,100,True,'cyan'))

packer.pack(
    bigger_first=False,
    distribute_items=True,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.9,

)
packer.putOrder()
b = packer.bins[0]
painter = Painter(b)
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
fig = painter.plotBoxAndItems(
    title=b.partno,
    alpha=0.8,
    write_num=False,
    fontsize=10
)
fig.show()














