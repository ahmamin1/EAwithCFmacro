import requests
import csv
import json
import math
import pandas as pd
import attMacro


# change this data and run the code
with open('config.json', 'r') as f:
    config = json.load(f)

groupID = config['groupID']
contestID = config['contestID']
page = config['page']
sessionID = config['sessionID']


api_url = f"https://codeforces-api.netlify.app/.netlify/functions/ac/g/{groupID}/c/{contestID}/p/{page}"
response = requests.get(api_url)

if response.status_code == 200:
    json_data = response.json()
    python_obj = json.dumps(json_data)
    obj = json.loads(python_obj)
    handels = list(obj['result']['contestants'].keys())
    solved = []
    for i in range(len(handels)):
        solved.append(
            math.ceil(len(obj['result']['contestants'][handels[i]]['ac'])/2))
    with open("output.csv", "w", newline='') as out:
        wr = csv.writer(out)
        wr.writerow(["Handle", "Solved"])
        for i in range(len(handels)):
            wr.writerow([handels[i], solved[i]])

    # merage report of contest with easy attend ids on cf handle
    df1 = pd.read_csv('dataset.csv')
    df2 = pd.read_csv('output.csv')
    merged_df = pd.merge(df1, df2, on='Handle')
    merged_df['easyattendID'] = merged_df['easyattendID'].apply(
        lambda x: pd.to_numeric(x, errors='coerce')).fillna(0).astype(int)

    merged_df.to_csv('report.csv', index=False)

    # run macro 
    attMacro.macro(sessionID)

else:
    print(f"Error: {response.status_code}")

