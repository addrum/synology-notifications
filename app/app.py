import json
import logging
import os
import requests
import sys
import traceback

from flask import Flask, request
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

def send(data):
    payload = {
        "content": data,
        "username": username
    }

    print(payload)

    response = requests.post(url, data=payload)

    print(f'response {response.reason}, {response.status_code}')

    return response.reason, response.status_code

@app.route('/', methods = ['GET'])
def home_get():
    body = request.args.get('text')
    print(f'text {body}')

    return send(body)

@app.route('/', methods = ['POST'])
def home_post():
    body = request.data
    if not body:
        return 'bad request', 400

    print(f'json {body}')

    try:
        synology_message = json.loads(body)['message']
        print(f'synology_message {synology_message}')
    except:
        return 'body not json', 400

    return send(synology_message)

if __name__ == '__main__':
    url = os.getenv('WEBHOOK_URL', None)
    if not url:
        print('No WEBHOOK_URL env var set!')
        sys.exit(1)

    username = os.getenv('USERNAME', 'synology')

    # Debug/Development
    app.run(debug=True, host="0.0.0.0", port="8686")
    # Production
    # http_server = WSGIServer(('', 8686), app)
    # http_server.serve_forever()