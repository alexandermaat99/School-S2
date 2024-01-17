import pandas as pd
import json

df = pd.read_csv('/Users/alexandermaat/Downloads/insurance.csv')

json_str = df.to_json(orient='columns')
json_str

df_json = json.loads(json_str)
# print(df_json['age']['2'])
# for k, v in df_json.items():
#     print(k, v)


json_str = df.to_json(orient='split')
df_json = json.loads(json_str)
print(df_json.keys())  

# for k, v in df_json.items():
#     print(k, v) 

print(df_json['data'][1][2])