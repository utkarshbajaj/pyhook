from flask import Flask
from flask import request
import os

app = Flask(__name__)
app.config['INTEGRATIONS'] = ['ACTIONS_ON_GOOGLE']

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(req)

if __name__ == '__main__':

    port = int(os.getenv('PORT', 5060))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')