from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
<<<<<<< HEAD

from .DBUser import User
=======
from database import DBUser

>>>>>>> 76048cdb085460f6437faab48b173e1396586faf
import re
import os

app = Flask(__name__)

client = MongoClient('localhost')#27017
db = client.local

# Secret key to use a session
app.config['SECRET_KEY'] = 'F34TF$($e34D';

Bootstrap(app)

@app.route("/")
<<<<<<< HEAD
def index():
	return render_template('register.html')
=======
def index():   
    return render_template('uservalidation.html')
>>>>>>> 76048cdb085460f6437faab48b173e1396586faf

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



# Sessions allows you to store information specific to a user from one request to the next
# To use a session you need a secret key

# @app.route() is by default limited to GET requests
# Allowed HTTP methods of an action can be specified using the methods keyword arg.
@app.route('/login', methods=['POST'])
def login():
<<<<<<< HEAD
    try: 
        client.insertUser("1","1","1","1","1","1")
        session['email'] = request.form['email']
        session['password'] = request.form['password']

        print 'user created'
=======
    #validate in DB
        
    # DBUser.insertUser("1",request.form['email'],request.form['password'],"1","1","admin")
    session['email'] = request.form['email']
    session['password'] = request.form['password']
>>>>>>> 76048cdb085460f6437faab48b173e1396586faf
    return redirect(url_for('message'))
    # user = DBUser.authenticateUser(request.form['email'], request.form['password'])
    # if user:
    #     return redirect(url_for('index'))

    # else:
    #     return redirect(url_for('login.html'))


# @app.route('/register', methods=['GET','POST'])
# def register():



# @app.route('/register', methods=['POST', 'GET'])
# def register():
#     if request.method == 'POST':
#         users = mongo.db.users
#         existing_user = users.find_one({'email' : request.form['email']})

#         if existing_user is None:
#             hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
#             users.insert({'name' : request.form['username'], 'password' : hashpass})
#             session['username'] = request.form['username']
#             return redirect(url_for('index'))
        
#         return 'That username already exists!'

#     return render_template('register.html')


@app.route('/message')
def message():
    if not 'email' in session:
        return abort(403)
    return render_template('/unused/message.html', email=session['email'], 
                                           password=session['password'])
# @app.route('/register', methods=['POST'])
# def register():

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return index()


    
if __name__ == "__main__":
    app.run(debug=True)