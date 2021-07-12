import json
import sqlite3

with open('C:/Users/homeg/Desktop/information.json', encoding = 'utf-8') as f:
    information = json.load(f)

color_set = []
color_set_two = []
for i in information:
    if i['mall'] == "SSF":
        color_set.append(i['color'])
        if i['color'] == "살구색":
            i['color'] = "주황색"
            i['color_detail'] = "살구색"
        elif i['color'] == "황토색":
            i['color'] = "갈색"
            i['color_detail'] = "황토색"
        elif i['color'] == "자주색":
            i['color'] = "보라색"
            i['color_detail'] = "자주색"
        elif i['color'] == "연보라색":
            i['color'] = "보라색"
            i['color_detail'] = "연보라색"
        elif i['color'] == "레몬":
            i['color'] = "노란색"
            i['color_detail'] = "레몬"
        elif i['color'] in ['솔리드', '플로럴', '아가일', '그라데이션', '애니멀', '깅엄', '타이포그래피', '타탄', '가로 스트라이프', '그래픽']:
            if i['pattern'] is None:
                i['pattern'] = i['color']
            # print(i['product_name'])
            title = i['product_name']
            if '회색' in title or 'GREY' in title or 'GRAY' in title or 'grey' in title or 'gray' in title or 'Gray' in title or 'Grey' in title:
                i['color'] = '회색'
            elif ' 화이트' in title or 'WHITE' in title or 'white' in title or 'White' in title:
                i['color'] = '회색'
            elif '노란색' in title or 'YELLOW' in title or 'Yellow' in title or 'yellow' in title:
                i['color'] = '노란색'
            elif '핑크' in title or 'PINK' in title or 'Pink' in title or 'pink' in title:
                i['color'] = '핑크색'
            elif '베이지' in title or 'BEIGE' in title or 'Beige' in title or 'beige' in title:
                i['color'] = '베이지'
            elif '블랙' in title or 'BLACK' in title or 'Black' in title or 'black' in title:
                i['color'] = '검정색'
            elif '네이비' in title or 'NAVY' in title or 'Navy' in title or 'navy' in title:
                i['color'] = '파란색'
                i['color_detail'] = '남색'
            elif '블루' in title or 'BLUE' in title or 'Blue' in title or 'blue' in title:
                i['color'] = '파란색'
            elif '카키' in title or 'KHAKI' in title or 'Khaki' in title or 'khaki' in title:
                i['color'] = '갈색'
                i['color_detail'] = '카키'
            elif '아이보리' in title or 'IVORY' in title or 'Ivory' in title or 'ivory' in title:
                i['color'] = '흰색'
                i['color_detail'] = '아이보리'
            elif '올리브' in title or 'OLIVE' in title or 'Olive' in title or 'olive' in title:
                i['color'] = '초록색'
                i['color_detail'] = '올리브 그린'
            elif '브라운' in title or 'BROWN' in title or 'Brown' in title or 'brown' in title:
                i['color'] = '갈색'
            else:
                i['color'] = None
            # print(i['color'])
        if i['pattern'] == "플로럴":
            i['pattern'] = "플라워"
            i['pattern_detail'] = "플로럴"
        if i['pattern'] == '기타' and i['pattern_detail'] == '솔리드':
            temp = i['pattern']
            i['pattern'] = i['pattern_detail']
            i['pattern_detail'] = temp

redundancy = []
information_temp = []
for i in information:
    if i['product_id'] not in redundancy:
        redundancy.append(i['product_id'])
        information_temp.append(i)

information = information_temp

con = sqlite3.connect('cloth.db')
cur = con.cursor()
query = """create table Annotation (
    	product_id TEXT,
    	product_name TEXT,
    	brand TEXT,
		brand_product_id TEXT,
		sex TEXT,
		superCategory TEXT,
		midCategory TEXT,
		category TEXT,
		color TEXT,
		color_detail TEXT,
        pattern TEXT,
        pattern_detail TEXT,
		material TEXT,
		model_img TEXT,
		price TEXT,
		product_link TEXT,
		product_img TEXT,
		style TEXT,
		mall TEXT,
		tag TEXT,
		is_wear TEXT,
		is_recommend TEXT
)"""
cur.execute(query)
query = "insert into Annotation values (:product_id, :product_name, :brand, :brand_product_id, :sex, :superCategory, :midCategory, :category, :color, :color_detail, :pattern, :pattern_detail, :material, :model_img, :price, :product_link, :product_img, :style, :mall, :tag, :is_wear, :is_recommend)"
cur.executemany(query, information)
con.commit()
con.close()