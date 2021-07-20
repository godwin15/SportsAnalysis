#this is to find the league we want to use
import requests
import pandas as pd
import json


url = "https://v3.football.api-sports.io/leagues/seasons"
headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e59dd673e0cb32c7063131d84c8649d"
    }

response = requests.request("GET", url, headers=headers)
#print(response.text)
rep = response.json()
print(rep)