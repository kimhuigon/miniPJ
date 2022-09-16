from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://dubardin:du6ardin@cluster0.j5xdh6l.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/utkwv", methods=["GET"])
def utkwv_get():
    utkwv_list = list(db.utkwv.find({}, {'_id': False}))
    return jsonify({'utkwvs': utkwv_list})

@app.route("/utktl", methods=["GET"])
def utktl_get():
    utktl_list = list(db.utktl.find({}, {'_id': False}))
    return jsonify({'utktls': utktl_list})

@app.route("/utkml", methods=["GET"])
def utkml_get():
    utkml_list = list(db.utkml.find({}, {'_id': False}))
    return jsonify({'utkmls': utkml_list})

@app.route("/utkwl", methods=["GET"])
def utkwl_get():
    utkwl_list = list(db.utkwl.find({}, {'_id': False}))
    return jsonify({'utkwls': utkwl_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)