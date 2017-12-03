from pymongo import MongoClient
import re

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local


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
        if not checkName(name):
            print 'INVALID'
        #print '\nInserted data successfully\n'
    
    except Exception, e:
        print str(e)

def checkName(name):
    if re.match("^[a-zA-Z0-9_.-]+$", name):
        raise Exception('Invalid letters/numbers')

def deleteUser(name):
    try:
	
	    db.User.delete_many({"name":name})

            if not name:
                raise Exception('Name cannot be empty')
		
	    print '\nDeletion successful\n'
		
    except Exception, e:
	    print str(e)



#def insertWorkshopGroup(name, description, type, skill_level, published_date, session_type):
#def deleteWorkshopGroup(name):
#def updateWorkshopGroup(name):

#def insertWorkshopUnit(name, description, type, skill_level, published_date, session_type, connection_string_type):
#def deleteWorkshopUnit(name):
#def updateWorkshopUnit(name):

def main():
    
    while(1):
    # choosing option to do CRUD operations
        selection = raw_input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
		  
    
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
            update()
        elif selection == '3':
            read()
        elif selection == '4':
		
            name = raw_input('Enter name to delete :')
            deleteUser(name)
        else:
            print '\n INVALID SELECTION \n'
			
if __name__ == '__main__':
   main()			
# Function to insert data into mongo db
