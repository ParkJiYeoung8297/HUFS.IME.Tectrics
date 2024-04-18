from py3dbp import Packer, Bin, Item, Painter
import time
start = time.time()

def update_item_colors(bins):
    for bin in bins:
        for item in bin.items:
            x = item.position[0]
            z = item.position[2]

            # Assign colors based on both x and z coordinates using hex codes
            if x <= 400:
                if z <= 700:
                    item.color = '#8B0000'  
                else:
                    item.color = '#FF6666'  

            elif 400 < x <= 800:
                if z <= 700:
                    item.color = '#006400'  
                else:
                    item.color = '#90EE90'  

            elif 800 < x <= 1200:
                if z <= 700:
                    item.color = '#00008B'  
                else:
                    item.color = '#ADD8E6'  

            elif 1200 < x <= 1600:
                if z <= 700:
                    item.color = '#CCCC00'  
                else:
                    item.color = '#FFFACD'  

            else:
                if z <= 800:
                    item.color = '#800080'  
                else:
                    item.color = '#E6E6FA'  

packer = Packer()

box1 = Bin('container 1',(2600, 1600, 1500), 100,0,0)

packer.addBin(box1)
boxes = [
 {
  "id": 0,
  "box_code": 558896584132,
  "cus_name": "이지영",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "112동 704호",
  "phone_num": "01023883578",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 1,
  "box_code": 7896230945860,
  "cus_name": "박미주",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 601호",
  "phone_num": "01093575243",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 2,
  "box_code": 3163664461359,
  "cus_name": "김나은",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1620동 1302호",
  "phone_num": "01094225194",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 3,
  "box_code": 6882455601865,
  "cus_name": "조도연",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "103동 1503호",
  "phone_num": "01055464537",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 4,
  "box_code": 9281590493123,
  "cus_name": "오호운",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 804호",
  "phone_num": "01076303989",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 5,
  "box_code": 5175882447873,
  "cus_name": "김이원",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 1005호",
  "phone_num": "01045734150",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 6,
  "box_code": 3700736297191,
  "cus_name": "김연경",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1606동 104호",
  "phone_num": "01026677091",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 7,
  "box_code": 8183256000119,
  "cus_name": "김성운",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1603동 101호",
  "phone_num": "01078283278",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 8,
  "box_code": 2874054606466,
  "cus_name": "한혀원",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 1804호",
  "phone_num": "01039607219",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 9,
  "box_code": 4685999482321,
  "cus_name": "권지지",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "103동 1002호",
  "phone_num": "01037519267",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 10,
  "box_code": 5876331852976,
  "cus_name": "장미서",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 1902호",
  "phone_num": "01054048750",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 11,
  "box_code": 8230870744990,
  "cus_name": "이견하",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1609동 101호",
  "phone_num": "01062915471",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 12,
  "box_code": 5018704565375,
  "cus_name": "강미비",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1615동 504호",
  "phone_num": "01044298669",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 13,
  "box_code": 5759744002868,
  "cus_name": "김상중",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 2002호",
  "phone_num": "01024671065",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 14,
  "box_code": 6692348032305,
  "cus_name": "김혀운",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 1804호",
  "phone_num": "01061192373",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 15,
  "box_code": 4339937388172,
  "cus_name": "김미비",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 303호",
  "phone_num": "01014586715",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 16,
  "box_code": 1962889683118,
  "cus_name": "오명비",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1605동 1301호",
  "phone_num": "01028654741",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 17,
  "box_code": 8448776383074,
  "cus_name": "김성지",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "103동 902호",
  "phone_num": "01091175434",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 18,
  "box_code": 8017232007345,
  "cus_name": "신은윤",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1610동 303호",
  "phone_num": "01032607399",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 19,
  "box_code": 4882179800274,
  "cus_name": "박재하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 2003호",
  "phone_num": "01043289835",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 20,
  "box_code": 4273770945834,
  "cus_name": "유주연",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "101동 1802호",
  "phone_num": "01080532694",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 21,
  "box_code": 718765033534,
  "cus_name": "남대영",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1613동 1203호",
  "phone_num": "01090688076",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 22,
  "box_code": 6674447892733,
  "cus_name": "손서윤",
  "address": "경기도 광주시 태전중앙로 20",
  "detail_address": "작심스터디카페 광주태전점",
  "phone_num": "01018532588",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 23,
  "box_code": 7566188691155,
  "cus_name": "김유저",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1615동 1704호",
  "phone_num": "01081353521",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 24,
  "box_code": 3363206028493,
  "cus_name": "이서하",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 302호",
  "phone_num": "01018783937",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 25,
  "box_code": 3877275268503,
  "cus_name": "천영수",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 1102호",
  "phone_num": "01065919348",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 26,
  "box_code": 8247169981962,
  "cus_name": "홍수연",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1601동 901호",
  "phone_num": "01076201532",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 27,
  "box_code": 1951131620934,
  "cus_name": "최시이",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 304호",
  "phone_num": "01079160930",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 28,
  "box_code": 5531853011977,
  "cus_name": "원세숭",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "112동 1205호",
  "phone_num": "01081252593",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 29,
  "box_code": 7247680487498,
  "cus_name": "강소서",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 1901호",
  "phone_num": "01029359988",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 30,
  "box_code": 7782528941377,
  "cus_name": "조아하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1606동 1601호",
  "phone_num": "01085886242",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 31,
  "box_code": 8509206532833,
  "cus_name": "조서예",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 701호",
  "phone_num": "01075832382",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 32,
  "box_code": 546463463753,
  "cus_name": "안평찬",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 1803호",
  "phone_num": "01045180033",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 33,
  "box_code": 9992305237336,
  "cus_name": "우찬섭",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1603동 701호",
  "phone_num": "01066689846",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 34,
  "box_code": 8515526317405,
  "cus_name": "유다리",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "101동 2002호",
  "phone_num": "01031016060",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 35,
  "box_code": 7153651189126,
  "cus_name": "송병연",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1605동 302호",
  "phone_num": "01071661004",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 36,
  "box_code": 3022415943442,
  "cus_name": "김주하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1606동 903호",
  "phone_num": "01085408279",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 37,
  "box_code": 9886867369624,
  "cus_name": "이성청",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 1102호",
  "phone_num": "01024117404",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 38,
  "box_code": 8468148483038,
  "cus_name": "이다연",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1604동 1304호",
  "phone_num": "01058075835",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 39,
  "box_code": 5400764552319,
  "cus_name": "장혀하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1603동 503호",
  "phone_num": "01061419939",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 40,
  "box_code": 3037709594742,
  "cus_name": "김준하",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 601호",
  "phone_num": "01046985837",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 41,
  "box_code": 5203781058594,
  "cus_name": "임승연",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 902호",
  "phone_num": "01090820198",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 42,
  "box_code": 6074114600794,
  "cus_name": "신균하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1603동 702호",
  "phone_num": "01036056299",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 43,
  "box_code": 4699118670600,
  "cus_name": "김하원",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1611동 1202호",
  "phone_num": "01068357090",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 44,
  "box_code": 7353273975274,
  "cus_name": "이미비",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "112동 1602호",
  "phone_num": "01081241897",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 45,
  "box_code": 2892952162829,
  "cus_name": "김미소",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1604동 1604호",
  "phone_num": "01080350631",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 46,
  "box_code": 4240588500692,
  "cus_name": "김혀원",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1616동 1804호",
  "phone_num": "01024385171",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 47,
  "box_code": 9237401272059,
  "cus_name": "김하지",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "104동 201호",
  "phone_num": "01078334541",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 48,
  "box_code": 9506362554555,
  "cus_name": "김수원",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1604동 402호",
  "phone_num": "01047070501",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 49,
  "box_code": 3636997467880,
  "cus_name": "최하미",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "104동 505호",
  "phone_num": "01084015198",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 50,
  "box_code": 6365440733338,
  "cus_name": "정미비",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 1605호",
  "phone_num": "01049104000",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 51,
  "box_code": 452036662376,
  "cus_name": "장미하",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 402호",
  "phone_num": "01030239437",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 52,
  "box_code": 6682544753841,
  "cus_name": "이세번",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1603동 601호",
  "phone_num": "01080695991",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 53,
  "box_code": 4416429234482,
  "cus_name": "강수서",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 1002호",
  "phone_num": "01075143320",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 54,
  "box_code": 8154194314813,
  "cus_name": "김지나",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 403호",
  "phone_num": "01036953007",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 55,
  "box_code": 1024403351829,
  "cus_name": "유은하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "101동 103호",
  "phone_num": "01090294374",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 56,
  "box_code": 1769997627838,
  "cus_name": "강도준",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 1401호",
  "phone_num": "01056825347",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 57,
  "box_code": 6963108854165,
  "cus_name": "김지정",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1613동 1402호",
  "phone_num": "01017722528",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 58,
  "box_code": 9986696791709,
  "cus_name": "방보은",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1610동 1501호",
  "phone_num": "01052228113",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 59,
  "box_code": 7340916057710,
  "cus_name": "임혀하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "101동 1502호",
  "phone_num": "01041976836",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 60,
  "box_code": 2816901855543,
  "cus_name": "손정우",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 1102호",
  "phone_num": "01081439172",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 61,
  "box_code": 1874795202670,
  "cus_name": "지잔연",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1611동 903호",
  "phone_num": "01074584412",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 62,
  "box_code": 995587410175,
  "cus_name": "오나하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 903호",
  "phone_num": "01059722861",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 63,
  "box_code": 7437759209871,
  "cus_name": "박하하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 1401호",
  "phone_num": "01083456553",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 64,
  "box_code": 7759571375336,
  "cus_name": "이혀주",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 2002호",
  "phone_num": "01028831930",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 65,
  "box_code": 7108577060594,
  "cus_name": "김수미",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 503호",
  "phone_num": "01097581901",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 66,
  "box_code": 3137387065824,
  "cus_name": "양성지",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 1805호",
  "phone_num": "01064739792",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 67,
  "box_code": 3822708727601,
  "cus_name": "이미영",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 1901호",
  "phone_num": "01022764012",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 68,
  "box_code": 4012165425923,
  "cus_name": "이하비",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 1603호",
  "phone_num": "01030850088",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 69,
  "box_code": 3178137363274,
  "cus_name": "김동균",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "103동 405호",
  "phone_num": "01027615488",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 70,
  "box_code": 1912205318986,
  "cus_name": "오서견",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "104동 1701호",
  "phone_num": "01086147473",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 71,
  "box_code": 1616219718814,
  "cus_name": "이하은",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "101동 201호",
  "phone_num": "01039241457",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 72,
  "box_code": 739683863860,
  "cus_name": "박지하",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1618동 1201호",
  "phone_num": "01098906709",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 73,
  "box_code": 1834813418821,
  "cus_name": "유미준",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 1401호",
  "phone_num": "01053845032",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 74,
  "box_code": 8030117709672,
  "cus_name": "윤승하",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 301호",
  "phone_num": "01015644746",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 75,
  "box_code": 4535594840173,
  "cus_name": "김예비",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1609동 402호",
  "phone_num": "01099642193",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 76,
  "box_code": 2331764586998,
  "cus_name": "김태운",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1620동 1304호",
  "phone_num": "01039443637",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 77,
  "box_code": 8359051457110,
  "cus_name": "김동운",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1613동 1501호",
  "phone_num": "01019920917",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 78,
  "box_code": 6278811220255,
  "cus_name": "서전하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1601동 104호",
  "phone_num": "01075887660",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 79,
  "box_code": 3441206773487,
  "cus_name": "이서지",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 1101호",
  "phone_num": "01048846299",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 80,
  "box_code": 4477403441111,
  "cus_name": "이성하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 605호",
  "phone_num": "01055405499",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 81,
  "box_code": 5410033935974,
  "cus_name": "김유하",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 101호",
  "phone_num": "01058591161",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 82,
  "box_code": 3653580272518,
  "cus_name": "이지연",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1604동 2004호",
  "phone_num": "01071401603",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 83,
  "box_code": 1848821694173,
  "cus_name": "이지연",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1619동 302호",
  "phone_num": "01081224395",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 84,
  "box_code": 6836840550294,
  "cus_name": "정기미",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1606동 301호",
  "phone_num": "01068686888",
  "length": 350,
  "width": 250,
  "height": 100
 },
 {
  "id": 85,
  "box_code": 2657883799100,
  "cus_name": "박이하",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 1302호",
  "phone_num": "01088842397",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 86,
  "box_code": 6560481989062,
  "cus_name": "박성연",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1616동 401호",
  "phone_num": "01075494464",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 87,
  "box_code": 8089373578317,
  "cus_name": "이수재",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 602호",
  "phone_num": "01045844804",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 88,
  "box_code": 5750016879668,
  "cus_name": "한승하",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1616동 1602호",
  "phone_num": "01051438670",
  "length": 480,
  "width": 380,
  "height": 340
 },
 {
  "id": 89,
  "box_code": 1741393668408,
  "cus_name": "강소은",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 1802호",
  "phone_num": "01047192632",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 90,
  "box_code": 7169826969422,
  "cus_name": "김운서",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 1403호",
  "phone_num": "01012031545",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 91,
  "box_code": 9463990019061,
  "cus_name": "문지완",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "102동 1901호",
  "phone_num": "01040956952",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 92,
  "box_code": 9057811021244,
  "cus_name": "류미미",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 1402호",
  "phone_num": "01050763966",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 93,
  "box_code": 707395096240,
  "cus_name": "오하연",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 403호",
  "phone_num": "01012910670",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 94,
  "box_code": 6952591988865,
  "cus_name": "이재균",
  "address": "경기도 광주시 태성로 107",
  "detail_address": "1602동 1201호",
  "phone_num": "01054705183",
  "length": 410,
  "width": 310,
  "height": 280
 },
 {
  "id": 95,
  "box_code": 8801039917565,
  "cus_name": "이지준",
  "address": "경기도 광주시 태성로 130",
  "detail_address": "1617동 301호",
  "phone_num": "01060261210",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 96,
  "box_code": 897064404880,
  "cus_name": "김선하",
  "address": "경기도 광주시 태성1로 16",
  "detail_address": "111동 503호",
  "phone_num": "01052631738",
  "length": 270,
  "width": 100,
  "height": 150
 },
 {
  "id": 97,
  "box_code": 7558253732180,
  "cus_name": "정다주",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1612동 704호",
  "phone_num": "01065341042",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 98,
  "box_code": 9241744980894,
  "cus_name": "박지비",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1614동 702호",
  "phone_num": "01057735499",
  "length": 340,
  "width": 350,
  "height": 210
 },
 {
  "id": 99,
  "box_code": 4009202434559,
  "cus_name": "김수연",
  "address": "경기도 광주시 태봉로 176",
  "detail_address": "1609동 103호",
  "phone_num": "01049777108",
  "length": 480,
  "width": 380,
  "height": 340
 }
 
]

# colors = ['red','yellow','lawngreen','cyan','brown','violet']
# for i, box in enumerate(boxes, start = 1):
#     width, height, depth = box ['dimension']
#     color_group = (i-1) //34
#     color_index = color_group % len(colors)
#     color = colors[color_index]
#     packer.addItem(Item(f'test{i}', 'test', 'cube', (width, height, depth), 1,i//34+1, 100,True, color ))
colors = ['red','yellow','lawngreen','cyan','violet']
for i, box in enumerate(boxes, start = 1):
    width, height, depth = box ['length'], box['width'], box['height']
    color_group = (i-1) // 20
    color_index = color_group % len(colors)
    color = colors[color_index]
    packer.addItem(Item(f'test{i}', 'test', 'cube', (width, height, depth), 1, i//5+1, 1000,True, color )) 


# calculate packing 
packer.pack(
    bigger_first=True,
    distribute_items=False,
    fix_point=True,
    check_stable=True,
    support_surface_ratio=0.65
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
#print("***************************************************")
# print("UNFITTED ITEMS:")
# for item in b.unfitted_items:
#     print("partno : ",item.partno)
#     print("color : ",item.color)
#     print("W*H*D : ",str(item.width) +'*'+ str(item.height) +'*'+ str(item.depth))
#     print("volume : ",float(item.width) * float(item.height) * float(item.depth))
#     print("weight : ",float(item.weight))
#     volume_f += float(item.width) * float(item.height) * float(item.depth)
#     unfitted_name += '{},'.format(item.partno)
#     print("***************************************************")
# print("***************************************************")
# print('space utilization : {}%'.format(round(volume_t / float(volume) * 100 ,2)))
# print('residual volumn : ', float(volume) - volume_t )
# print('unpack item : ',unfitted_name)
# print('unpack item volumn : ',volume_f)
# print("gravity distribution : ",b.gravity)
# stop = time.time()
# print('used time : ',stop - start)

painter = Painter(b)
fig = painter.plotBoxAndItems(
    title=b.partno,
    alpha=0.9,
    write_num=False,
    fontsize=10
)
fig.show()