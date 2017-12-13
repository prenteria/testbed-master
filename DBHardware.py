from pymongo import MongoClient
import re

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local



def addServer(ip, username, password):
    try:

        print '\Adding Server: \n'
        db.Server.insert_one(
            {
            "username": username,
            "password": password,
            "ip": ip
            
            })

    except Exception, e:
        print str(e)


def deleteServer(ip):
    try:

        print '\Deleting Server: \n'
        db.Server.delete_many(
            {
            "ip": ip
            
            })

    except Exception, e:
        print str(e)

#def addUnitToWorkshop(unit_id, workshop_group_id)

def updateServer(ip, username, password):
    try:

        print '\Updating Server: ' , ip
        result = db.Server.update_one(
            {"ip" : str(ip)},
            {
           "$set" : {
           "ip" : ip,
            "username": username,
            "password": password
            }})

    except Exception, e:
        print str(e)


    except Exception, e:
        print str(e)

def addVM(name, vrdp, adapter, ip, snapshot):
    try:

        print '\Adding VM'
        result = db.VM.insert_one(
            {
            "name": name,
            "vrdp": vrdp,
            "adapter": adapter,
            "ip" : ip,
            "snapshot" : snapshot,

            "Server" : [
                         { 
                            "ip" : ip,

                         }

                        ]
            })

    except Exception, e:
        print str(e)


def deleteVM(name):
    try:

        print '\Deleting VM: ' , name
        result = db.VM.delete_many(
            {
            "name" : name
            })

    except Exception, e:
        print str(e)


def updateVM(name, vrdp, adapter, ip, snapshot):
    try:

        print '\Updating VM: ' , name
        result = db.VM.update_one(
            {"name" : str(name)},
            {
            "$set" : {
            "name" : name,
            "vrdp": vrdp,
            "adapter": adapter,
            "ip" : ip,
            "snapshot" : snapshot,

            "Server" : [
                         { 
                            "ip" : ip,

                         }

                        ]

            }})

    except Exception, e:
        print str(e)

def main():

    while(1):
    # choosing option to do CRUD operations
        selection = raw_input('\nSelect 1 to add VM, 2 to update VM, 3 to read VM, 4 to delete VM\n')
    
        if selection == '1':
            name = raw_input('Enter VM name :')
        
    	    if not name:
                raise Exception('name cannot be empty')
		       

            vrdp = raw_input('Enter vrdp :')

            if not vrdp:
                raise Exception('vrdp cannot be empty')
                      

            adapter = raw_input('Enter adapter :')

            if not adapter:
                raise Exception('adapter cannot be empty')


            ip = raw_input('Enter server ip :')

            snapshot = raw_input('Enter snapshot date :')
                      

            addVM(name, vrdp, adapter, ip, snapshot)
            
        elif selection == '2':

            name = raw_input('Enter VM name :')
        
               
            vrdp = raw_input('Enter vrdp :')

            
            adapter = raw_input('Enter adapter :')

            ip = raw_input('Enter ip :')

            snapshot = raw_input('Enter snapshot date :')

        
            updateVM(name, vrdp, adapter, ip, snapshot)



        elif selection == '3':
            read()
        elif selection == '4':
		
            name = raw_input('Enter name to delete :')
            deleteVM(name)

        else:
            print '\n INVALID SELECTION \n'
			
if __name__ == '__main__':
   main()			
# Function to insert data into mongo db
