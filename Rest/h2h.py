import requests
import pandas as pd
import json
from sqlalchemy import create_engine
import sqlalchemy
import os
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


#dictionary having the teams & their ID's
team_ids = {"Manchester United":"33", "Newcastle":"34","Bournemouth":"35","Fulham":"36","Huddersfield":"37","Watford":"38","Wolves":"39","Liverpool":40,
           "Southampton":"41","Arsenal":"42","Burnley":'44',"Everton":45, "Leicester":46, "Tottenham": 47, "West Ham":48, "Chelsea":49,
						"Manchester City": 50, "Brighton":51, "Crystal Palace":52, "Reading":53, "Brentford":55,"Leeds":63,"Aston Villa":66,"Norwich":71}
               

#url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h=33-34"

'''
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       #continue
    else:
       return userInput 
       break'''


id_1 = input("put the team1 id: ")
	
id_2 = input("put the team2 id: ")

url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h="+str(id_1)+"-"+str(id_2)

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "15bfd3d0f2da9bf0cbe8370c0dbed2f4"
    }

r = requests.request("GET", url, headers=headers)
rep = r.json()
#print(rep['response'][0]['teams']['home']['winner'])

#for i in range(20):
  #print(rep['response'][i]['teams']['home']['name'], 'played', rep['response'][i]['teams']['away']['name'],'on', rep['response'][i]['fixture']['date']) 
  #hometeam.append(rep['response'][i]['teams']['home']['winner'])
  #awayteam.append(rep['response'][i]['teams']['away']['winner'])
  
#print(hometeam)
#print(awayteam)

#DataFrame
#Creating a dictionary to obtain the data we want for the dataframe
data = {"Home Team": [rep["response"][i]['teams']['home']['name'] for i in range(len(rep["response"]))],
			 "Away Team":[rep["response"][i]['teams']['away']['name'] for i in range(len(rep["response"]))],
			 "Date_and_Time": [rep['response'][i]['fixture']['date'] for i in range(len(rep["response"]))],
			 "Win Status HomeTeam": [rep['response'][i]['teams']['home']['winner'] for i in range(len(rep["response"]))],
			 "Win Status AwayTeam": [rep['response'][i]['teams']['away']['winner'] for i in range(len(rep["response"]))]}

#CREATING A DATAFRAME FOR THE FIXTURE
df = pd.DataFrame(data, columns = ['Home Team', 'Away Team', 'Date_and_Time','Win Status HomeTeam','Win Status AwayTeam'])
print(df)

#engine = create_engine('sqlite:///OurDatabase.db')
#df.to_sql("headTohead", engine)

name_1 = rep["response"][0]['teams']['home']['name']
name_2 = rep["response"][0]['teams']['away']['name']
win_1 = 0
win_2 = 0
draws = 0

for i in range(len(rep["response"])):
    if name_1 == rep["response"][i]['teams']['home']['name']:
        if rep['response'][i]['teams']['home']['winner'] == True:# counting the wins for name_1
            win_1 += 1
        if rep['response'][i]['teams']['home']['winner'] == None: #counting the draws for both
            draws += 1
    if name_1 == rep["response"][i]['teams']['away']['name']:
        if rep['response'][i]['teams']['away']['winner'] == True: # counting the wins for name_1
            win_1 += 1
        if rep['response'][i]['teams']['away']['winner'] == None:
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
print('')



x = [name_1,name_2,"Draws"]
y = [win_1,win_2,draws]

plt.bar(x,y)
plt.savefig("Plot2.png")












'''
#Creating dataset
marks = np.array([win_1,win_2])

# Creating histogram
fig, ax = plt.subplots(1, 1)
ax.hist(marks)

# Set title
ax.set_title("Fixture Analysis Chart")

# adding labels
ax.set_xlabel('Results')
ax.set_ylabel('Frequency')

# Make some labels.
rects = ax.patches
labels = [name_1,name_2]

for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width() / 2, height+1, label,
			ha='center', va='bottom')

#Show plot
#plt.show()
plt.savefig("Plotter.png")


histogram = [win_1,win_2,draws]
plt.bar(range(len(histogram)),histogram)
#histogram.plot()
plt.savefig("bar.png")
'''

'''
dict_f = {name_1: [win_1], name_2: [win_2], "Draws": [draws]}
df3 = pd.DataFrame(dict_f, columns = [name_1,name_2,"Draws"])
'''
