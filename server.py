from flask import Flask, render_template, Response, request, redirect, url_for
import requests 
import os 


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

#background process happening without any refreshing
@app.route('/hunter')
def hunter():
    res = requests.get("http://178.128.130.13:5984/users/jhgaylor")
    output = res.content
    print(output)
    return output

@app.route('/enumerate', methods=['POST'])
def forward():
    res = requests.get("http://178.128.130.13:5984/users/jhgaylor")
    output = res.content
    return render_template('index.html', Enumerate_data=output);
