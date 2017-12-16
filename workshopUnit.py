from Workshop import workshop
from Server import Server
from VirtualMachine import VirtualMachine
import datetime
#(workshop)
class workshopUnit(workshop):
    def __init__(self,name,description,host,skillLevel,publishedDate,sessionType,vm):
        workshop.__init__(self,name,description,host,skillLevel,publishedDate,sessionType)
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
    def getVirtualMachineList(self):
        return self.vm
    def setConnectionString(self,string):
        self.connectionString=string
    def setVirtualMachineList(self,list):
        self.vm=list
    def addVirtualMachineToUnit(self,vmToAdd):
        self.vm.append(vmToAdd)
    def getVMstatus(self):
        return self.vm.getStatus()
    #def getPersistenceDate(self):

    #def getSessionState(self):
     #   return server.getSessionState()

    #def setSessionState(self):
    def restoreUnit(self):
        for v in self.vm:
            if(v.getCurrentSnapshot()!=""):
                v.hostName.restore_snapshot(v.getName())

    def cloneWorkshop(self,name,numClones,vrdpSeed,netAdptrSeed):
        serv=Server("10.0.0.0","user","pass")
        clonedUnits=[]
        totalVmClones=[]
        cloneList=[]
        for v in self.vm:
            #tempList=hardware.cloneVM(v.getName(),vrdpSeed,netAdptrSeed,1)
            tempList = serv.cloneVM(v.getName(), vrdpSeed, netAdptrSeed, numClones)
            totalVmClones=totalVmClones+tempList

        index = 0
        clonesUsed = 0
        while (clonesUsed < numClones):
            index=clonesUsed
            while index+numClones < len(totalVmClones):
                cloneList.append(totalVmClones[index])
                cloneList.append(totalVmClones[index + numClones])
                index += 1
            newName=name+"("+str(clonesUsed+1)+")"
            newWorkshopUnit = workshopUnit(newName, self.description, self.host, self.skillLevel, datetime.datetime.now(),self.sessionType, totalVmClones)
            clonedUnits.append(newWorkshopUnit)
            clonesUsed += 1
        return clonedUnits

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