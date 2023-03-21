from flask import Flask
import requests 

app = Flask(__name__)


@app.route('/space')
def space():
    r = requests.get('https://api.spacexdata.com/v2/launches')
    r.json()
    return r.content

@app.route('/womens')
def womens():
    r = requests.get('https://women-in-tech.apievangelist.com/apis/people/')
    r.json()
    return r.content

