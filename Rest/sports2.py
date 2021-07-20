import requests
import pandas as pd
import json
import sqlalchemy
from sqlalchemy import create_engine
import os

#DICTIONARY WITH TEAM IDS
team_ids = {"Manchester United":"33", "Newcastle":"34","Bournemouth":"35","Fulham":"36","Huddersfield":"37","Watford":"38","Wolves":'39',"Liverpool":'40',
           "Southampton":'41',"Arsenal":'42',"Burnley":'44',"Everton":'45', "Leicester":'46', "Tottenham": '47', "West Ham":'48', "Chelsea":'49',
						"Manchester City": '50', "Brighton":'51', "Crystal Palace":'52', "Reading":'53', "Brentford":'55',"Leeds":'63',"Aston Villa":'66',"Norwich":'71'}


#getting fixtures, dates and times for the next season.
url = "https://v3.football.api-sports.io/fixtures?league=39&season=2021"

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "15bfd3d0f2da9bf0cbe8370c0dbed2f4"
    }

r = requests.request("GET", url, headers=headers)
rep = r.json()
#for i in range(len(rep["response"])):
  #print(rep["response"][i]['teams']['home']['name'], "will play", rep["response"][i]['teams']['away']['name'], "on ", rep['response'][i]['fixture']['date'])

			#Creating a dictionary to obtain the data we want for the dataframe
data = {"Home Team": [rep["response"][i]['teams']['home']['name'] for i in range(len(rep["response"])) if i < 20],
			 "Away Team":[rep["response"][i]['teams']['away']['name'] for i in range(len(rep["response"])) if i < 20],
			 "Date_and_Time": [rep['response'][i]['fixture']['date'] for i in range(len(rep["response"])) if i < 20]}

#CREATING A DATAFRAME FOR THE FIXTURE
df = pd.DataFrame(data, columns = ['Home Team', 'Away Team', 'Date_and_Time'])
print(df)

#CHOOSING THE FIXTURE
fixture_choice = input('Choose the fixture index, (0-19): ')
fixture_choice = int(fixture_choice)
home_team = rep["response"][fixture_choice]['teams']['home']['name']
away_team = rep["response"][fixture_choice]['teams']['away']['name']

#GETTING ID'S FROM THE DICTIONARY TO BE PASSED INTO THE HEAD TO HEAD FUNCTION
id_1 = team_ids[home_team]
id_2 = team_ids[away_team]

#print(id1)
#print(id2)

url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h="+id_1+"-"+id_2

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "15bfd3d0f2da9bf0cbe8370c0dbed2f4"
    }

r = requests.request("GET", url, headers=headers)
rep = r.json()


#Creating a dictionary to obtain the data we want for the dataframe
data = {"Home Team": [rep["response"][i]['teams']['home']['name'] for i in range(len(rep["response"]))],
			 "Away Team":[rep["response"][i]['teams']['away']['name'] for i in range(len(rep["response"]))],
			 "Date_and_Time": [rep['response'][i]['fixture']['date'] for i in range(len(rep["response"]))],
			 "Win Status HomeTeam": [rep['response'][i]['teams']['home']['winner'] for i in range(len(rep["response"]))],
			 "Win Status AwayTeam": [rep['response'][i]['teams']['away']['winner'] for i in range(len(rep["response"]))]}

#CREATING A DATAFRAME FOR THE FIXTURE
df = pd.DataFrame(data, columns = ['Home Team', 'Away Team', 'Date_and_Time','Win Status HomeTeam','Win Status AwayTeam'])
print(df)


name_1 = rep["response"][0]['teams']['home']['name']
name_2 = rep["response"][0]['teams']['away']['name']
win_1 = 0
win_2 = 0
draws = 0 
                                                                      
#print("The team at mewins)
for i in range(len(rep["response"])):
    if name_1 == rep["response"][i]['teams']['home']['name']:
        if rep['response'][i]['teams']['home']['winner'] == True:# counting the wins for name_1
            win_1 += 1
        if rep['response'][i]['teams']['home']['winner'] == None: #counting the draws for both
            draws += 1
    if name_1 == rep["response"][i]['teams']['away']['name']:
        if rep['response'][i]['teams']['away']['winner'] == True: # counting the wins for name_1
            win_1 += 1
        if rep['response'][i]['teams']['away']['winner'] == None: #counting the draws for both
            draws += 1
    if name_2 == rep["response"][i]['teams']['away']['name']:
        if rep['response'][i]['teams']['away']['winner'] == True: # counting the wins for name_2
            win_2 += 1

    if name_2 == rep["response"][i]['teams']['home']['name']:
        if rep['response'][i]['teams']['home']['winner'] == True: # counting the wins for name_2
            win_2 += 1
				
print('Team '+name_1+' won '+str(win_1)+' times')	
print('Team '+name_2+' won ' +str(win_2)+ ' times')
print('Both Teams drew ' +str(draws)+ ' times')
