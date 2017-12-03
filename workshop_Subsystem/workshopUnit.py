from Workshop import workshop
#from Server import server
import datetime
#(workshop)
class workshopUnit(workshop):
    def __init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,vm):
        workshop.__init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial)
        self.vm=vm
        self.connectionString=''
        self.connectionStringType=''
    def vmStatus(self):
        self.vm.getStatus()
    def getConnectionString(self):
        return self.connectionString
    def getConnectionStringType(self):
        return self.connectionStringType
    def setConnectionStringType(self,type):
        self.connectionStringType=type
        #go to hardware 5
    def setConnectionString(self,string):
        self.connectionString=string
    def getVitualMachineList(self):
        return self.vm
    def setVitualMachineList(self,list):
        self.vm=list
    def addVirtualMachineToUnit(self,vmToAdd):
        self.vm.append(vmToAdd)
    def getVMstatus(self):
        return self.vm.getStatus()
    #def getPersistenceDate(self):

    #def getSessionState(self):
     #   return server.getSessionState()

    #def setSessionState(self):

    def cloneWorkshop(self,name,numClones,vrdpSeed,netAdptrSeed):
        newVM=self.vm.clone(self.vm,vrdpSeed,netAdptrSeed,numClones)
        newWorkshopUnit=workshopUnit(name,self.name,self.description,self.status,self.host,self.skillLevel,datetime.datetime.now(),self.sessionType,self.refMaterial,newVM)
        return newWorkshopUnit

    def exportWorkshop(self, selectedWorkshopList):
        index=0
        while index < len(selectedWorkshopList):
            info = open(selectedWorkshopList[index].name + ".txt", "w+")
            info.write(selectedWorkshopList[index].name + "\n")
            info.write(selectedWorkshopList[index].description + "\n")
            info.write(selectedWorkshopList[index].status + "\n")
            info.write(selectedWorkshopList[index].host + "\n")
            info.write(selectedWorkshopList[index].skillLevel + "\n")
            info.write(selectedWorkshopList[index].publishedDate + "\n")
            info.write(selectedWorkshopList[index].sessionType + "\n")
            info.close()
            #find way to move ova file and all ref material
            index = index + 1

    def importWorkshop(self, name, description, rm, persistenceType, workshop, workshopList):
        index=0
        while index < len(workshopList):
            info=open(workshopList[index]+"txt","r")
            workshop.setName(info.readline())
            workshop.setDescription(info.readline())
            workshop.setStatus(info.readline())
            workshop.setHost(info.readline())
            workshop.setSkillLevel(info.readline())
            workshop.setPublishedDate(info.readline())
            workshop.setSessionType(info.readline())
            workshopList.append(workshop)

            index=index+1