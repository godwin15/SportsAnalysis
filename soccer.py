import requests
import pandas as pd
import json
import sqlalchemy
from sqlalchemy import create_engine
import os
from matplotlib import pyplot as plt
import numpy as np

#getting fixtures, dates and times for the next season.
print('')
print("       WELCOME TO SPORTS ANALYSIS!!")
print("Here are the first 20 match-ups for next season:\n")

#HEADERS FUNCTION
def header():
	headers = {
	'x-rapidapi-host': "v3.football.api-sports.io",
	'x-rapidapi-key': "15bfd3d0f2da9bf0cbe8370c0dbed2f4"
	}
	return headers

#Input validation
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 	

def leaguefixtures():
	
	url = "https://v3.football.api-sports.io/fixtures?league=39&season=2021"
	headers = header()
	r = requests.request("GET", url, headers=headers)
	rep = r.json()
	return rep

#To be called in the main function
def fixturedf(rep):
	#rep = leaguefixtures()
	#Creating a dictionary to obtain the data we want for the dataframe
	data = {"Home Team": [rep["response"][i]['teams']['home']['name'] for i in range(len(rep["response"])) if i < 20],
				 "Away Team":[rep["response"][i]['teams']['away']['name'] for i in range(len(rep["response"])) if i < 20],
				 "Date_and_Time": [rep['response'][i]['fixture']['date'] for i in range(len(rep["response"])) if i < 20]}

	#CREATING A DATAFRAME FOR THE FIXTURE
	df = pd.DataFrame(data, columns = ['Home Team', 'Away Team', 'Date_and_Time'])
	#print(df)
	return df

#CHOOSING THE FIXTURE
def fixturechoice(rep):
	
	#rep = leaguefixtures()
	fixture_choice = inputNumber('Choose the fixture index, (0-19): ')
	fixture_choice = int(fixture_choice)
	home_team = rep["response"][fixture_choice]['teams']['home']['name']
	away_team = rep["response"][fixture_choice]['teams']['away']['name']
	
	return (home_team, away_team)

#GETTING ID'S FROM THE DICTIONARY TO BE PASSED INTO THE HEAD TO HEAD FUNCTION
def teamIDs(name1,name2):
	#DICTIONARY WITH TEAM IDS
	team_ids = {"Manchester United":"33", "Newcastle":"34","Bournemouth":"35","Fulham":"36",
				"Huddersfield":"37","Watford":"38","Wolves":'39',"Liverpool":'40',"Southampton":'41',
				"Arsenal":'42',"Burnley":'44',"Everton":'45', "Leicester":'46', "Tottenham": '47', "West Ham":'48',
				"Chelsea":'49',"Manchester City": '50', "Brighton":'51', "Crystal Palace":'52', "Reading":'53', "Brentford":'55',
				"Leeds":'63',"Aston Villa":'66',"Norwich":'71'}
	#teamname = fixturechoice()
	id_1 = team_ids[name1]
	id_2 = team_ids[name2]
	
	return id_1, id_2

#getting the h2h meetings
def headtohead(id1,id2):
	#I_D = teamIDs()
	url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h="+id1+"-"+id2

	headers = header()

	r = requests.request("GET", url, headers=headers)
	rep = r.json()
	return rep

#getting the dataframe and presenting
def dataframeheadtohead(rep):
	#rep = headtohead() 
	#Creating a dictionary to obtain the data we want for the dataframe
	data = {"Home Team": [rep["response"][i]['teams']['home']['name'] for i in range(len(rep["response"]))],
				 "Away Team":[rep["response"][i]['teams']['away']['name'] for i in range(len(rep["response"]))],
				 "Date_and_Time": [rep['response'][i]['fixture']['date'] for i in range(len(rep["response"]))],
				 "Win Status HomeTeam": [rep['response'][i]['teams']['home']['winner'] for i in range(len(rep["response"]))],
				 "Win Status AwayTeam": [rep['response'][i]['teams']['away']['winner'] for i in range(len(rep["response"]))]}

	#CREATING A DATAFRAME FOR THE FIXTURE
	df = pd.DataFrame(data, columns = ['Home Team', 'Away Team', 'Date_and_Time','Win Status HomeTeam','Win Status AwayTeam'])
	#print(df)
	return df

#GETTING THE WINS AND DRAWS
def wins_draws(rep):
	
	#rep = headtohead() #we will figure this out
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

	return win_1, win_2, draws	

#Finding probality of the team to win
def probability(win1,win2,draws):
	p_team1 = win1/(win1+win2+draws)
	p_team2 = win2/(win1+win2+draws)
	p_draws = draws/(win1+win2+draws)
	return (p_team1,p_team2,p_draws)
	
#MAIN FUNCTION
def main():
	rep = leaguefixtures()
	d_f = fixturedf(rep)
	print(d_f)
	print('')
	home,away = fixturechoice(rep)
	id_1,id_2 = teamIDs(home,away)
	repjson = headtohead(id_1,id_2)
	dframe = dataframeheadtohead(repjson)
	print('')
	print("   ***Head to Head matches of your choosen fixture*** ")
	print('')
	print(dframe)
	print('')
	
	win1,win2,draw = wins_draws(repjson)
	total = win1+win2+draw
	print("Team "+home+" won "+str(win1)+" out of "+str(total)+" matches")
	print("Team "+away+" won "+str(win2)+" out of "+str(total)+" matches")
	print('')
	p1,p2,p3 = probability(win1,win2,draw)
	print("    ^^What are the Odds^^ \n")
	print('The chances of team '+home+' to win are '+str(p1))
	print('The chances of team '+away+' to win are '+str(p2))
	print('The chances for a draw are '+str(p3))
	print('')
	#Plotting the Histogram
	x = [home,away,"Draws"]
	y = [win1,win2,draw]

	plt.bar(x,y)
	plt.ylabel("Frequency")
	plt.title("Team Analysis Chart")
	plt.savefig("soccer.png")
	
	print('   ***Now you can BET***')
	print('')
	#Goodbye message
	
if __name__ == "__main__":
    main()
