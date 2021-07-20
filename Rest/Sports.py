##pseudocode for sports analysis

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


#ID1 = input("Enter the first team ID: ")
#ID2 = input("Enter the second team ID: ")


#url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h="+ID1+"-"+ID2+"&season=2020"

url = "https://v3.football.api-sports.io/fixtures?league=39&season=2019"

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e59dd673e0cb32c7063131d84c8649d"
    }

r = requests.request("GET", url, headers=headers)
#print(response.text)
rep = r.json()
#print(rep)
#for data in rep['response']:
#print(rep['response']['teams']['home']['name']
      
print(rep['response']

  