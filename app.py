from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_bootstrap import Bootstrap
# from pymongo import MongoClient
# from database import DBUser
import re
import os

# app = Flask(__name__, static_url_path="/static", static_folder='/testbed-master/static')

app = Flask(__name__)

# client = MongoClient('localhost')#27017
# db = client.local

# Secret key to use a session
app.config['SECRET_KEY'] = 'F34TF$($e34D';

Bootstrap(app)

@app.route("/")
def index():
	return render_template('uservalidation.html')

@app.route("/home")
def home():
	return render_template('index.html')


@app.route("/servers")
def server():
    return render_template('server.html')

@app.route("/vms")
def virtualmachine():
    return render_template('virtualmachines.html')

@app.route("/workshopunits")
def workshopunits():
    return render_template('workshopunits.html')

@app.route('/workshopgroups')
def workshopgroups():
    return render_template('workshopgroups.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/userprofiles')
def userprofiles():
    return render_template('userprofiles.html')

@app.route('/persistence')
def persistence():
    return render_template('persistenceworkshops.html')

@app.route('/temporary')
def temporary():
    return render_template('temporaryworkshops.html')

# Sessions allows you to store information specific to a user from one request to the next
# To use a session you need a secret key

# @app.route() is by default limited to GET requests
# Allowed HTTP methods of an action can be specified using the methods keyword arg.
@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    return redirect(url_for('home'))

@app.route('/register', methods=['POST'])
def register():
    session['firstname'] = request.form['firstname']
    session['lastname'] = request.form['lastname']
    session['organization'] = request.form['organization']
    session['lastname'] = request.form['lastname']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    return redirect(url_for('persistence'))

@app.route('/message')
def message():
    if not 'email' in session:
        return abort(403)
    return render_template('/unused/message.html', email=session['email'], 
                                           password=session['password'])

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()

    
if __name__ == "__main__":
    app.run(debug=True)