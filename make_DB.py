import sqlite3
import json

with open('C:/Users/homeg/Desktop/recommend.json', encoding = 'utf-8') as f:
    recommend = json.load(f)
with open('C:/Users/homeg/Desktop/information.json', encoding = 'utf-8') as f:
    information = json.load(f)
with open('C:/Users/homeg/Desktop/wear.json', encoding = 'utf-8') as f:
    wear = json.load(f)
print(information[0])
print(len(information[0]))
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
		fit TEXT,
		mall TEXT,
		tag TEXT,
		is_wear TEXT,
		is_recommend TEXT
)"""
cur.execute(query)
query = "insert into Annotation values (:product_id, :product_name, :brand, :brand_product_id, :sex, :superCategory, :midCategory, :category, :color, :color_detail, :pattern, :pattern_detail, :material, :model_img, :price, :product_link, :product_img, :style, :fit, :mall, :tag, :is_wear, :is_recommend)"
cur.executemany(query, information)
con.commit()
con.close()


con = sqlite3.connect('recommend.db')
cur = con.cursor()
query = """create table Recommend (
		product_id TEXT,
		recommend_id TEXT,
		product_category TEXT,
		recommend_category TEXT,
		recommend_number TEXT,
		mall TEXT
)"""
cur.execute(query)
query = "insert into Recommend values (:product_id, :recommend_id, :product_category, :recommend_category, :recommend_number, :mall)"
cur.executemany(query, recommend)
con.commit()
con.close()

con = sqlite3.connect('wear.db')
cur = con.cursor()
query = """create table Wear (
        codi_num TEXT,
    	product_id TEXT,
		category TEXT,
		style TEXT,
		product_img TEXT,
		model_img TEXT,
		url TEXT,
		upper_color TEXT,
		bottom_color TEXT,
		mall TEXT
)"""
cur.execute(query)
query = "insert into Wear values (:codi_num, :product_id, :category, :style, :product_img, :model_img, :url, :upper_color, :bottom_color, :mall)"
cur.executemany(query, wear)
con.commit()
con.close()