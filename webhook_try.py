import json
from googleapiclient.discovery import build

api_key = 'AIzaSyCHzECS8mqw065KiT3A0yAMZWxd86gfgEc'

youtube = build('youtube', 'v3', developerKey = api_key)

request = youtube.channels().list(
        part="statistics",
        forUsername="sentdex"
    )

response = request.execute()

res = json.dumps(response, sort_keys=True, indent=4)

print(response['items'][0]['statistics']['subscriberCount'])

#print(response)

#response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Mumbai&units=metric&appid=1b483ab5ef2cb6f6241a26d2295cf9bc")
