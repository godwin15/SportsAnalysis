''' HEAD TO HEAD FUNCTION
def head2head(id_1, id_2):
	
	url = "https://v3.football.api-sports.io/fixtures/headtohead?h2h="+id_1+"-"+id_2

	headers = {
    		'x-rapidapi-host': "v3.football.api-sports.io",
    		'x-rapidapi-key': "15bfd3d0f2da9bf0cbe8370c0dbed2f4"
   			}

	re = requests.request("GET", url, headers=headers)
	repr = re.json()
	data = { "Home Team":[repr["response"][i]['teams']['home']['name'] for i in range(len(rep["response"]))],
           "Away Team":[repr["response"][i]['teams']['away']['name'] for i in range(len(rep["response"]))],
           "Date_and_Time":[repr['response'][i]['fixture']['date'] for i in range(len(rep["response"]))],
           "Win Status HomeTeam": [repr['response'][i]['teams']['home']['winner'] for i in range(len(rep["response"]))],
           "Win Status AwayTeam": [repr['response'][i]['teams']['away']['winner'] for i in range(len(rep["response"]))]}

	df1 = pd.DataFrame(data, columns = ['ID','Home Team', 'Away Team', 'Date_and_Time','Win Status HomeTeam','Win Status AwayTeam'])
	
	return df1
'''



'''GETTING THE DATABASE
database_name = "Head-to-head-fixtures"
table_name = "Head-to-head"
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
os.system('mysql -u -root -pcodio '+database_name+' < '+table_name)
engine = create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')
df.to_sql(table_name, con=engine, if_exists='replace', index = False)
os.system('mysqldump -u root -pcodio '+database_name+' > '+ table_name)'''






'''
#engine = create_engine('sqlite:///OurDatabase.db')
#df.to_sql("headTohead", engine)

#dataf = head2head(id1,id2)

#print(dataf)

#GETTING INPUT FROM THE USER SO THEY CAN PICK A FIXTURE FROM THE LIST OF MATCH UPS GETTING
#fixture_id = input("What end-to-end match ups would you like to see?(type the fixture id): ") #include error handliing

#CREATING ANOTHER API CALL FOR H2H MEETINGS

#CREATING A PROBABILITY FUNCTION
def probability(wins_1,wins_2,draws):
	total = wins_1 + wins_2 + draws
	p_team1 = wins_1/total
	p_team2 = wins_2/total
	p_draw = draws/total
	return (p_team1, p_team2,p_draw)


#CREATING A PIE CHART PLOT

homewins = [rep['response'][i]['teams']['home']['winner'] for i in range(len(rep["response"]))]  
awaywins = [rep['response'][i]['teams']['away']['winner'] for i in range(len(rep["response"]))] 
'''






from matplotlib import pyplot as plt
import numpy as np

# Creating dataset
marks = np.array([70, 50, 40, 90, 55, 85, 74, 66, 33, 11, 45, 36, 89])

# Creating histogram
fig, ax = plt.subplots(1, 1)
ax.hist(marks)

# Set title
ax.set_title("Title")

# adding labels
ax.set_xlabel('x-label')
ax.set_ylabel('y-label')

# Make some labels.
rects = ax.patches
labels = ["label%d" % i for i in range(len(rects))]

for rect, label in zip(rects, labels):
	height = rect.get_height()
	ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
			ha='center', va='bottom')

# Show plot
plt.show()
