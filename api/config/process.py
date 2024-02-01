import pandas as pd
import sqlite3

# Read csv file.
df = pd.read_csv(r"C:\Users\user\Desktop\BE_AI_GO\api\config\202309.csv", encoding='cp949')

# Connect to (create) database.
database = r"C:\Users\user\Desktop\BE_AI_GO\api\db.sqlite3"
conn = sqlite3.connect(database)
dtype={
    "name": "CharField",
    "image": "ImageField",
    "branch": "CharField", 
    "classification": "CharField",
    "industry_classification": "CharField",
    "city_county": "CharField",
    "Administrative": "CharField", 
    "legal": "CharField",
    "adress": "TextField",
    "building": "CharField",
    "street_name_address": "TextField", 
    "zip_code": "CharField",
    "floor": "IntegerField",
    "hardnesss": "FloatField",
    "latitude": "FloatField", 
    "info": "TextField",
    "like": "IntegerField",
}
df.to_sql(name='places_place', con=conn, if_exists='replace', dtype=dtype, index=True, index_label="id")
conn.close()
