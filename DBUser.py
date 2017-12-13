from pymongo import MongoClient
import re

# creating connections for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local


def read():
    try:
        users = db.User.find()
        print '\n ALL USERS \n'
        for user in users:
            print user

    except Exception, e:
        print str(e)

def authenticateUser(email, password):
        try:

            users = db.User.find(
                {
                "email": email,
                "password": password
                 })
            count = 0
            for user in users:
                count = count +1
            if count > 0:
                return True
            else:
                return False

        except Exception, e:
            print str(e)

        print '\n User: ' , email


def insertUser(self,name, email, password, orginization, skill_level, user_type):
        try:
            
            print '\Inserting: \n'
            db.User.insert_one(
                {
                "name": name,
                "email":email,
                "password":password,
                "orginization":orginization,
            "skill_level":skill_level,
                "user_type":user_type
                })
            if not checkName(name):
                print 'INVALID'
            #print '\nInserted data successfully\n'
        
        except Exception, e:
            print str(e)

def checkName(self,name):
        if re.match("^[a-zA-Z0-9_.-]+$", name):
            raise Exception('Invalid letters/numbers')


def updateUser(self,name, email, password, orginization, skill_level, user_type, user_id):
        try:

            print '\Updating user: ' , user_id, name
            result = db.User.update_one(
                {"_id" : int(user_id)},
                {
               "$set" : {
               "name": name ,
                "email": email,
                "password": password,
                "orginization": orginization,
                "skill_level": skill_level,
                "user_type": user_type
                }})

        except Exception, e:
            print str(e)

def deleteUser(self,name):
        try:
        
            db.User.delete_many({"name":name})

            if not name:
                raise Exception('Name cannot be empty')
            
            print '\nDeletion successful\n'
            
        except Exception, e:
            print str(e)
