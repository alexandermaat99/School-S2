import pandas as pd
import json
import sqlite3

df = pd.read_csv('/Users/alexandermaat/Downloads/insurance.csv')

# create the database
conn = sqlite3.connect('insurance.db')

# create the table
create_sql = 'create table if not exists customers (age integer, sex text, bmi real, children integer, smoker text, region text, charges real)'
cursor = conn.cursor()
cursor.execute(create_sql)


# insert data into the table itterating through each line
for row in df.itertuples():
    insert_sql = f"insert into customers (age, sex, bmi, children, smoker, region, charges) \
        values ({row[1]},'{row[2]}',{row[3]},{row[4]},'{row[5]}','{row[6]}',{row[7]})"
    cursor.execute(insert_sql)

# comit the change
conn.commit()


#the faster way to do it 
df.to_sql(name='customers', con = conn, if_exists='replace', index=False)

# read from sqlite, needed for the assignemnt 

import sqlite3
conn = sqlite3.connect('insurance.db')


# change sql statement to change the output
read_sql = 'select * from customers'
cursor = conn.cursor()
results = cursor.execute(read_sql)

# print(results.fetchone())

df_new = pd.read_sql(read_sql, conn)
# print(df_new.head())


# GET STARTED ON API

import requests

response = requests.get('https://api.publicapis.org/entries')
# print(response.text)
results = json.loads(response.text)
print(results)





