from flask import Flask, render_template, jsonify, request, redirect, session
import json
import requests
import distutils.util
import os
import random
import string
import time
import urllib.parse
import jwt
import redis
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('mongodb://Hailey:0202@15.164.228.14', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('main.html')


@app.route('/logout', methods=['GET'])
def logout():
    return render_template('home.html')


@app.route('/main')
def main():
    return render_template('main.html')


@app.route('/friends')
def friends():
    return render_template('friends.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
