import requests as r, json, pandas as pd


# step 1 make the request
res = r.get('http://api.publicapis.org/entries')
# print(res.text)

# 2 convert to json dictionary
res_json = json.loads(res.text)
# print(res_json)


# 3 identify the data that we want as a json type and convert back to json string

str_json = json.dumps(res_json['entries'])


# import json string into a new dataframe
# df = pd.read_json(str_json)
# print(df.head())

import sys
sys.path.append('/Users/alexandermaat/Documents/GitHub/School-S2')
import myLibrary as fun

# fun.univariate(df)


# new call
url = "https://api.agify.io?name=alexander"

res = r.get(url)
# print(res.text)

# new call
url = "https://api.genderize.io?name=alexander"

res = r.get(url)
# print(res.text)

# new call
url = "https://api.nationalize.io?name=alexander"

res = r.get(url)
# print(res.text)

data = {
    "Inputs":  {
        "input1":{
            "ColumnNames": ["Marital Status", "Gender", "Income", "Children", "Cars", "Age", "Education", "Occupation", "Home Owner", "Commute Distance", "Region"],
            "Values": [["Married", "Male", "2000000", "2", "2", "50", "Graduate", "Professional", "Yes", "0-1 Miles", "North America"],
                       ["Married", "Male", "50000", "3", "2", "20", "Graduate", "Professional", "Yes", "10-15 Miles", "South America"]]
        }
    }
}

body = str.encode(json.dumps(data))

key = 'j++I0waAENjH+TGR4oynHqUBlSMEwuiUoS0fQ2ZJFYbG73USnTQSsXkIU9kmfUSkjvC9OHU3LQXGMceG+vPdZA=='
url = "https://ussouthcentral.services.azureml.net/workspaces/ddab2c5151cf4c44ad08dc0a26a7aa17/services/f5bd9d43e84741a5b0536c25ebf6b288/execute?api-version=2.0&details=true"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

res = r.post(url = url, headers=headers, data = body)
# print(res.text)

res_json = json.loads(res.text)
print(res_json['Results']['output1']['value']['Values'][0][0])
print(res_json['Results']['output1']['value']['Values'][1][0])
