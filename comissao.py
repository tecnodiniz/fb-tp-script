import os
import glob
import shutil
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_USER = os.getenv('MONGODB_USER')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE')

uri = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@localhost:27017"

client = MongoClient(uri)

db = client[MONGODB_DATABASE]

collection = db['comissoes']


path = "comissao/*.xlsx"
output = "backup/comissao/"
files = glob.glob(path)

dataframe = []

if len(files) >  0:
    for file in files:
        print(f"reading: {file}")
        
        df = pd.read_excel(file)
        df = df.drop(df.columns[0], axis=1)
        df['__file__'] = os.path.basename(file)

        dataframe.append(df)

        shutil.move(file, output + os.path.basename(file))


    df_final = pd.concat(dataframe, ignore_index=True)

    json_data = df_final.to_json(orient="records", indent=4, force_ascii=False)

    collection.insert_many(df_final.to_dict(orient="records"))

    print("Files saved on MongoDB")

    with open("comissao.json",  "w", encoding='utf-8') as f:
        f.write(json_data)


    print("Files saved as data.json")
else: 
    print("0 files to process")

