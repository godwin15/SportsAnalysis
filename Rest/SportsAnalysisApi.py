'''
- Using Football-api to get the fixtures for a a certain league 
- pesent the fixtures to the user for the them to choose a particular fixture
- requsting the head to head meetings of the selected fixture from api
- put the data in the database
- create a visual i.e., piechart using the data in the database
- Presenting the final conclusion on who is going to win!
'''

import requests
import pandas as pd
import json

#4e59dd673e0cb32c7063131d84c8649d
'''
url = "https://v3.football.api-sports.io/fixtures?live=all"
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e59dd673e0cb32c7063131d84c8649d"
    }

response = requests.request("GET", url, headers=headers)
#print(response.text)
rep = response.json()
print(rep.keys())'''

import http.client

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e59dd673e0cb32c7063131d84c8649d"
    }

conn.request("GET", "/teams?name=Barcelona", headers=headers)

res = conn.getresponse()
data = res.read()
print(data)




'''
response.json().keys() #checking keys of the response
response.json()['name'].keys()

# Create dictionary of results for 'leagues' key
names_dict = response.json()['api']['names']

names_df = pd.DataFrame.from_dict(names_dict)
display(names_df)

print(response.text'''


##############################################









