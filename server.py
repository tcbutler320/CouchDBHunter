from flask import Flask, render_template, Response, request, redirect, url_for
import requests 
import os 
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/use-cases')
def use():
    return render_template('use-cases.html')

@app.route('/installation')
def installation():
    return render_template('installation.html')

@app.route('/enumerate', methods=['GET','POST'])
def forward():
    target = request.form.get('target')
    database = request.form.get('database')
    document = request.form.get('document')
    if request.method == 'POST':
        if target and not database and not document:
            try:
                # target = "http://178.128.130.13:5984/_all_dbs"
                # target = "178.128.130.13"
                url = "http://" + str(target) + ":5984/_all_dbs"
                # print(url)
                res = requests.get(url)
                output = "Available Databases: "
                output += res.text
            except: 
                output = "oops error occured"
        elif target and database and not document:
            try:
                # target = "http://178.128.130.13:5984/_all_dbs"
                # target = "178.128.130.13"
                url = "http://" + str(target) + ":5984/" + database + "/_all_docs"
                # print(url)
                res = requests.get(url)
                output = "All Documents: "
                output += res.text
            except: 
                output = "oops error occured"
        elif target and database and document:
            try:
                # target = "http://178.128.130.13:5984/_all_dbs"
                # target = "178.128.130.13"
                url = "http://" + str(target) + ":5984/" + database + "/" + document
                # print(url)
                res = requests.get(url)
                output = "Documents " + document + ": "
                output += res.text
            except: 
                output = "oops error occured"
        else:
            output = "oops try putting an ip in first"
    else:
        output = "oops try putting an ip in first"
        
    return render_template('index.html', Enumerate_data=output);

@app.route('/enumerate_db', methods=['POST'])
def enumerate_db():
    try:
        res = requests.get("http://178.128.130.13:5984/users")
        output = "Database Documents: "
        output += res.text
    
    except: 
        output = "oops error occured"
    
    return render_template('index.html', database_data=output);

@app.route('/api/query')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route('/api/foo')
def json_example():
     # Create Dictionary
    value = {
        "firstName": "Pawan",
        "lastName": "Gupta",
        "hobbies": ["playing", "problem solving", "coding"],
        "age": 20,
        "children": [
            {
                "firstName": "mohan",
                "lastName": "bansal",
                "age": 15
            },
            {
                "firstName": "prerna",
                "lastName": "Doe",
                "age": 18
            }
        ]
    }
  
    # Dictionary to JSON Object using dumps() method
    # Return JSON Object
    return json.dumps(value)


# allow both GET and POST requests
@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        target = request.form.get('target')
        return '''
                  <h1>The target value is: {}</h1>'''.format(target)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Language: <input type="text" name="language"></label></div>
               <div><label>Framework: <input type="text" name="framework"></label></div>
               <input type="submit" value="Submit">
           </form>'''