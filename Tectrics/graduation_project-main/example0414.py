from py3dbp import Packer, Bin, Item, Painter
import time
start = time.time()

def update_item_colors(bins):
    for bin in bins:
        for item in bin.items:
            if item.position[0]  < 500:
                item.color = 'red'
            elif 500<= item.position[0]  <= 1000:
                item.color = 'yellow'
            elif 1000<= item.position[0]  <= 1500:
                item.color = 'green'
            elif 1500 <= item.position[0]  <= 2000:
                item.color = 'blue'
            else :
                item.color = 'violet'

packer = Packer()

box1 = Bin('Box1',(2700, 1600, 1800), 100,0,0)

packer.addBin(box1)
boxes = [
    {
        "id": 1,
        "box_code": "1001608940310",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 2,
        "box_code": "1255331667451",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 3,
        "box_code": "7808079316332",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 4,
        "box_code": "5671575018389",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 5,
        "box_code": "8638895986364",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 6,
        "box_code": "8032428131281",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 7,
        "box_code": "4309227211353",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 8,
        "box_code": "4148882021853",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 9,
        "box_code": "7834206831215",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 10,
        "box_code": "288904457333",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 11,
        "box_code": "5430370728308",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 12,
        "box_code": "5722403122228",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 13,
        "box_code": "9508605690321",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 14,
        "box_code": "7956753502458",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 15,
        "box_code": "497059917141",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 16,
        "box_code": "4363216948666",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 17,
        "box_code": "6226713810731",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 18,
        "box_code": "1300626663035",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 19,
        "box_code": "5308352107518",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 20,
        "box_code": "1283686388392",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 21,
        "box_code": "3716263958375",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 22,
        "box_code": "572928450542",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 23,
        "box_code": "7758478384217",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 24,
        "box_code": "4229780943984",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 25,
        "box_code": "3934706702541",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 26,
        "box_code": "3596253728429",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 27,
        "box_code": "2042183495390",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 28,
        "box_code": "8007212672037",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 29,
        "box_code": "1852467898747",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 30,
        "box_code": "1509262564243",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 31,
        "box_code": "906373346528",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 32,
        "box_code": "5601452160902",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 33,
        "box_code": "4270558063180",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 34,
        "box_code": "2480305075997",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 35,
        "box_code": "4935268907779",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 36,
        "box_code": "469577573004",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 37,
        "box_code": "9133774723578",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 38,
        "box_code": "7797920324903",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 39,
        "box_code": "1696209007287",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 40,
        "box_code": "9734373628261",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 41,
        "box_code": "4659494365648",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 42,
        "box_code": "7128402562415",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 43,
        "box_code": "303489282656",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 44,
        "box_code": "2359694192448",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 45,
        "box_code": "7787733031295",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 46,
        "box_code": "356962608929",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 47,
        "box_code": "119627255268",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 48,
        "box_code": "3266343120487",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 49,
        "box_code": "8106171398168",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 50,
        "box_code": "7122246587314",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 51,
        "box_code": "3415558702513",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 52,
        "box_code": "4494943412103",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 53,
        "box_code": "7999966334370",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 54,
        "box_code": "1794367986596",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 55,
        "box_code": "2968304401631",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 56,
        "box_code": "7330841886084",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 57,
        "box_code": "3633861139407",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 58,
        "box_code": "6746816377202",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 59,
        "box_code": "6129891374597",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 60,
        "box_code": "6526881091672",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 61,
        "box_code": "8890172274947",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 62,
        "box_code": "9225865859740",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 63,
        "box_code": "9632624431898",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 64,
        "box_code": "1881833792942",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 65,
        "box_code": "1565777220451",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 66,
        "box_code": "1059693462054",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 67,
        "box_code": "7845731350793",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 68,
        "box_code": "8389847643767",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 69,
        "box_code": "5200333850357",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 70,
        "box_code": "5964963149891",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 71,
        "box_code": "2460100127672",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 72,
        "box_code": "6887392577107",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 73,
        "box_code": "7594132199485",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 74,
        "box_code": "1013655071541",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 75,
        "box_code": "4402829155895",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 76,
        "box_code": "1168501926218",
        "dimension": [
            480,
            370,
            340
        ]
    },
    {
        "id": 77,
        "box_code": "2777708757425",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 78,
        "box_code": "2157270789853",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 79,
        "box_code": "1765840674296",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 80,
        "box_code": "2542192777596",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 81,
        "box_code": "6432818864540",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 82,
        "box_code": "9556298929749",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 83,
        "box_code": "1734422005991",
        "dimension": [
            180,
            160,
            70
        ]
    },
    {
        "id": 84,
        "box_code": "1361267004831",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 85,
        "box_code": "9444318620995",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 86,
        "box_code": "9783171159827",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 87,
        "box_code": "5938383148299",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 88,
        "box_code": "1707891500879",
        "dimension": [
            520,
            450,
            400
        ]
    },
    {
        "id": 89,
        "box_code": "4340146685698",
        "dimension": [
            270,
            180,
            150
        ]
    },
    {
        "id": 90,
        "box_code": "8175662132113",
        "dimension": [
            410,
            310,
            280
        ]
    },
    {
        "id": 91,
        "box_code": "3024090358057",
        "dimension": [
            520,
            480,
            400
        ]
    },
    {
        "id": 92,
        "box_code": "1230660781354",
        "dimension": [
            220,
            190,
            90
        ]
    },
    {
        "id": 93,
        "box_code": "9307860587193",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 94,
        "box_code": "3368261437706",
        "dimension": [
            320,
            240,
            200
        ]
    },
    {
        "id": 95,
        "box_code": "4783508251440",
        "dimension": [
            260,
            180,
            150
        ]
    },
    {
        "id": 96,
        "box_code": "6800165713357",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 97,
        "box_code": "2142776954424",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 98,
        "box_code": "7888410713895",
        "dimension": [
            600,
            500,
            450
        ]
    },
    {
        "id": 99,
        "box_code": "1363045751643",
        "dimension": [
            340,
            250,
            210
        ]
    },
    {
        "id": 100,
        "box_code": "7188595286934",
        "dimension": [
            270,
            180,
            150
        ]
    }
]

# colors = ['red','yellow','lawngreen','cyan','brown','violet']
# for i, box in enumerate(boxes, start = 1):
#     width, height, depth = box ['dimension']
#     color_group = (i-1) //34
#     color_index = color_group % len(colors)
#     color = colors[color_index]
#     packer.addItem(Item(f'test{i}', 'test', 'cube', (width, height, depth), 1,i//34+1, 100,True, color ))
colors = ['red','yellow','lawngreen','cyan','brown','violet']
for i, box in enumerate(boxes, start = 1):
    width, height, depth = box ['dimension']
    color_group = (i-1) // 15
    color_index = color_group % len(colors)
    color = colors[color_index]
    packer.addItem(Item(f'test{i}', 'test', 'cube', (width, height, depth), 1, i//15+1, 100,True, color )) 



# calculate packing 
packer.pack(
    bigger_first=True,
    distribute_items=False,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.6,
)

update_item_colors(packer.bins) 

# print result
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