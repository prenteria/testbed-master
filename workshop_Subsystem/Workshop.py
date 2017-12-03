#from Server import server
import datetime
class workshop:
    def __init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial):
        self.name=name
        self.description=description
        self.status=status
        self.host=host
        self.skillLevel=skillLevel
        self.publishedDate=publishedDate
        self.sessionType=sessionType
        self.refMaterial=refMaterial

    def deleteWorkshop(self,workshop,workshopList):
        workshopList.remove(workshop)

    def importWorkshop(self, name, description, rm, persistenceType, workshop, workshopList):
        workshop.name = name
        workshop.description = description
        workshop.refMaterial = rm
        workshop.sessionType = persistenceType
        workshopList.append(workshop)
    def cloneWorkshop(self,name,numClones,vrdpSeed,netAdptrSeed):
        newWorkshop=workshop(name,self.description,self.status,self.host,self.skillLevel,datetime.datetime.now(),self.sessionType)
        return newWorkshop

    #def exportWorkshop(self,selectedWorkshopList):



    def getName(self):
        return self.name
    def getDescription(self):
        return self.description
    #def getStatus(self):
     #   server.getSessionStatus()
    #def getHost(self):
     #   server.getIp()
    def getSkillLevel(self):
        return self.skillLevel
    def getPublishedDate(self):
        return self.publishedDate
    def getSessionType(self):
        return self.sessionType
    def getReferenceMaterial(self):
        return self.refMaterial
    def setName(self,newName):
        self.name=newName
    def setDescription(self,newDescription):
        self.description=newDescription
    def setSkillLevel(self,newSkillLevel):
        self.skillLevel=newSkillLevel
    def setReferenceMaterial(self,newReferenceMaterial):
        self.refMaterial=newReferenceMaterial
    def setSessionType(self,sessType):
        self.sessionType=sessType
    def setStatus(self,newStatus):
        self.status=newStatus
    def setHost(self,hostToSet):
        self.host=hostToSet
    def setPublishedDate(self,pd):
        self.publishedDate=pd

