from flask import Flask
from flask import request
import os
import json
from googleapiclient.discovery import build

api_key = 'AIzaSyCHzECS8mqw065KiT3A0yAMZWxd86gfgEc'

youtube = build('youtube', 'v3', developerKey = api_key)

app = Flask(__name__)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    return res


def processRequest(req):
    result = req.get("queryResult")
    parameters = result.get("parameters")
    username = parameters["username"]
    request = youtube.channels().list(
        part="statistics",
        forUsername=username
    )
    response = request.execute()
    totalNumber = response['items'][0]['statistics']['subscriberCount']
    return speech_output(totalNumber)

def speech_output(speech):
    return {
        "fulfillmentText": speech,
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": speech
                            }
                        }
                    ]

                }
            }
        }
    }

if __name__ == '__main__':

    port = int(os.getenv('PORT', 5060))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')