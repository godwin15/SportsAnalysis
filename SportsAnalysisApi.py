import http.client
import requests

url = "https://v3.football.api-sports.io/{endpoint}"

payload={}

headers = {
  'x-rapidapi-key': '4e59dd673e0cb32c7063131d84c8649d',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

############

conn = http.client.HTTPSConnection("v3.football.api-sports.io")

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "4e59dd673e0cb32c7063131d84c8649d"
    }

conn.request("GET", "/{endpoint}", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

