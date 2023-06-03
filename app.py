from flask import Flask,jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def index():
    return "<h1>Json Web Api</h1>"

@app.route("/youbike")
def youbike():
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.request('GET',url)
    response.encoding = 'utf-8'
    allData = response.json()
    return jsonify(allData)

@app.route("/youbike/<sarea>")
def sarea(sarea):
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.request('GET',url)
    allData = response.json()
    response.encoding = 'utf-8'
    areaData = [site for site in allData if site['sarea']==sarea]
    return jsonify(areaData)

