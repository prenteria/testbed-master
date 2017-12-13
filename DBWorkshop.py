from pymongo import MongoClient
import re

# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost')#27017
db = client.local



def insertWorkshopGroup(name, description, type, skill_level, published_date, session_type, unit_id):
    try:

        print '\Creating Workshop Group: \n'
        db.Workshop_Group.insert_one(
            {
            "name": name,
            "description": description,
            "type": type,
            "skill_level": skill_level,
            "published_date": published_date,
            "session_type": session_type,

            "Workshop_Unit" : [
                                {
                                    "_id" : unit_id,
                                }
                            ]
            })

    except Exception, e:
        print str(e)


def insertWorkshopUnit(name, description, type, skill_level, published_date, session_type, connection_type, vm_id):
    try:

        print '\Creating Workshop Unit: \n'
        db.Workshop_Unit.insert_one(
            {
            "name": name,
            "description": description,
            "type": type,
            "skill_level": skill_level,
            "published_date": published_date,
            "session_type": session_type,
            "connection_type": connection_type,

            "VM" : [
                                {
                                    "_id" : vm_id,
                                }
                            ]
            })

    except Exception, e:
        print str(e)

#def addUnitToWorkshop(unit_id, workshop_group_id)

def updateWorkshopGroup(name, description, type, skill_level, published_date, session_type, workshop_group_id):
    try:

        print '\Updating Workshop Group: ' , workshop_group_id, name
        result = db.Workshop_Group.update_one(
            {"_id" : int(workshop_group_id)},
            {
           "$set" : {
           "name": name ,
            "description": description,
            "type": type,
            "skill_level": skill_level,
            "published_date": published_date,
            "session_type": session_type
            }})


    except Exception, e:
        print str(e)


def updateWorkshopUnit(name, description, type, skill_level, published_date, session_type, connection_type, workshop_unit_id):
    try:

        print '\Updating Workshop Group: ' , workshop_unit_id, name
        result = db.Workshop_Unit.update_one(
            {"_id" : int(workshop_unit_id)},
            {
           "$set" : {
           "name": name ,
            "description": description,
            "type": type,
            "skill_level": skill_level,
            "published_date": published_date,
            "session_type": session_type,
            "connection_type": connection_type
            }})

        
    except Exception, e:
        print str(e)

def deleteWorkshopUnit(name):
    try:

        print '\Deleting workshop unit: ' , name

        db.Workshop_Unit.delete_many({"name":name})

    except Exception, e:
        print str(e)

def deleteWorkshopGroup(name):
    try:

        print '\Deleting workshop group: ' , name

        db.Workshop_Group.delete_many({"name":name})

    except Exception, e:
        print str(e)

def main():

    while(1):
    # choosing option to do CRUD operations
        selection = raw_input('\nSelect 1 to create worshop group, 2 to update group, 3 to read group, 4 to delete group\n')
    
        if selection == '1':
            name = raw_input('Enter workshop name :')
        
    	    if not name:
                raise Exception('Name cannot be empty')
		       

            description = raw_input('Enter description :')

            if not description:
                raise Exception('description cannot be empty')
                      

            type = raw_input('Enter type :')

            if not type:
                raise Exception('type cannot be empty')
                      

            skill_level = raw_input('Enter skill_level :')
         
            if not skill_level:
                raise Exception('skill_level cannot be empty')
                      

            published_date = raw_input('Enter published_date :')

            if not published_date:
                raise Exception('published_date cannot be empty')
                      

            session_type = raw_input('Enter session_type :')

            if not session_type:
                raise Exception('session_type cannot be empty')


            unit_id = raw_input('Enter workshop unit id :')

            if not unit_id:
                raise Exception('unit_id cannot be empty')


            connection_type = raw_input('Enter workshop unit id :')

            vm_id = raw_input('Enter workshop unit id :')
                      

            insertWorkshopUnit(name, description, type, skill_level, published_date, session_type, connection_type, vm_id)
            
        elif selection == '2':

            name = raw_input('Enter workshop name :')
        
               
            description = raw_input('Enter description :')

            
            type = raw_input('Enter type :')


            skill_level = raw_input('Enter skill_level :')
         
                      

            published_date = raw_input('Enter published_date :')
                      

            session_type = raw_input('Enter session_type :')

            connection_type = raw_input('Enter session_type :')


            workshop_unit_id = raw_input('Enter workshop_unit_id :')

            if not workshop_unit_id:
                raise Exception('workshop_unit_id cannot be empty')

        
            updateWorkshopUnit(name, description, type, skill_level, published_date, session_type, connection_type, workshop_unit_id)



        elif selection == '3':
            read()
        elif selection == '4':
		
            name = raw_input('Enter name to delete :')
            deleteWorkshopUnit(name)
        else:
            print '\n INVALID SELECTION \n'
			
if __name__ == '__main__':
   main()			
# Function to insert data into mongo db
