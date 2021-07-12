import sqlite3
import json

with open('C:/Users/homeg/Desktop/recommend.json', encoding = 'utf-8') as f:
    recommend = json.load(f)

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