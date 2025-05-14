import os
import glob
import shutil
import pandas as pd

path = "data/*.xlsx"
output = "backup/"
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

    with open("data.json",  "w", encoding='utf-8') as f:
        f.write(json_data)


    print("Files saved as data.json")
else: 
    print("0 files to process")