from pymongo import MongoClient
import re

# creating connections for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local


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


def read():
    try:
        users = db.User.find()
        print '\n ALL USERS \n'
        for user in users:
            print user

    except Exception, e:
        print str(e)



def insertUser(name, email, password, orginization, skill_level, user_type):
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
        
        print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)


def updateUser(name, email, password, orginization, skill_level, user_type, user_id):
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

def deleteUser(name):
        try:
        
            db.User.delete_many({"name":name})

            if not name:
                raise Exception('Name cannot be empty')
            
            print '\nDeletion successful\n'
            
        except Exception, e:
            print str(e)

def main():
    
    while(1):
    # choosing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to auth, 4 to delete\n')
		  
    
        if selection == '1':
            name = raw_input('Enter User name :')
        
    	    if not name:
                raise Exception('Name cannot be empty')
		       

            email = raw_input('Enter email :')

            if not email:
                raise Exception('Email cannot be empty')
                      

            password = raw_input('Enter password :')

            if not password:
                raise Exception('Password cannot be empty')
                      

            orginization = raw_input('Enter orginization :')
         
            if not orginization:
                raise Exception('Orginization cannot be empty')
                      

            skill_level = raw_input('Enter skill level :')

            if not skill_level:
                raise Exception('Skill level cannot be empty')
                      

            user_type = raw_input('Enter user_type :')

            if not user_type:
                raise Exception('User type cannot be empty')
                      

            insertUser(name, email, password, orginization, skill_level, user_type)
            
        elif selection == '2':

            name = raw_input('Enter User name :')

            email = raw_input('Enter email :')

            

            password = raw_input('Enter password :')

            
            orginization = raw_input('Enter orginization :')
         
            

            skill_level = raw_input('Enter skill level :')

            

            user_type = raw_input('Enter user_type :')

            user_id = raw_input('Enter user id :')

            if not user_id:
                raise Exception('user_id cannot be empty')

            
            updateUser(name, email, password, orginization, skill_level, user_type, user_id)


        elif selection == '3':

            email = raw_input('Enter email :')

            password = raw_input('Enter password :')

            isauth =  authenticateUser(email, password)
            if isauth:
                 print 'welcome'
            else:
                  print 'WRONG'
        elif selection == '4':
		
            name = raw_input('Enter name to delete :')
            deleteUser(name)
        else:
            print '\n INVALID SELECTION \n'
			
if __name__ == '__main__':
   main()			
# Function to insert data into mongo db
