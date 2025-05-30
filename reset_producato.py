import os
import glob
import re
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

collection = db['producao']

collection.delete_many({})


print('Tabela Produção resetada')