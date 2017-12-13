from Workshop import workshop
from workshopGroup import workshopGroup
from workshopUnit import workshopUnit
import re, subprocess
from ReferenceMaterial import ReferenceMaterial
class workshopManager:
    workshopGoupList=[]
    workshopUnitList=[]
    def updateWG(self,wg,name,description,status,host,skillLevel,publishedDate,sessionType,rm,wuList):
        wg.setName(name)
        wg.setDescription(description)
        wg.setStatus(status)
        wg.setHost(host)
        wg.setSkillLevel(skillLevel)
        wg.setPublishedDate(publishedDate)
        wg.setReferenceMaterial(rm)
        wg.setUnits(wuList)
        wg.setSessionType(sessionType)
    def updateWU(self,wu,name,description,status,host,skillLevel,publishedDate,rm,connectionString,persistenceType,vmList):
        wu.setName(name)
        wu.setDescription(description)
        wu.setStatus(status)
        wu.setHost(host)
        wu.setSkillLevel(skillLevel)
        wu.setPublishedDate(publishedDate)
        wu.setReferenceMaterial(rm)
        wu.setVirtualMachineList(vmList)
        wu.setSessionType(persistenceType)
        wu.setConnectionString(connectionString)
    def missingRequiredField(requiredField):
        return "Please fill out"+requiredField

    def deleteError(self,ws):
        if isinstance(ws, workshopUnit):
            return "Please select worskhop unit"
        if isinstance(ws,workshopGroup):
            return "Please select workshop group"
    def getReferenceMaterial(self,ws):
        ws.getReferenceMaterial()
    #def exportWorkshop(self):

    def createGroup(self,name,description,host,skillLevel,publishedDate,sessionType,units):
        wgList=self.getWorkshopGroupList()
        for wrkshpG in  wgList:
            if wrkshpG.name == name:
                return "Workshop group name is not unique"
        newWg= workshopGroup(name,description,host,skillLevel,publishedDate,sessionType,units)
        self.workshopGoupList.append(newWg)
        return newWg #delete
        #update database
    def createUnit(self,name,description,host,skillLevel,publishedDate,sessionType,vm):
        wuList=self.getWorkshopUnitList()
        for wrkshpU in  wuList:
            if wrkshpU.name == name:
                return "Workshop unit name is not unique"
        newWu=workshopUnit(name,description,host,skillLevel,publishedDate,sessionType,vm)
        self.workshopUnitList.append(newWu)
        return newWu #delete
        #update mongo
        #create unit add to list update db
    def addWorkshopG(self,ws):
        #wgL=self.getWorkshopGroupList()
        self.workshopGoupList=self.workshopGoupList+ws
        #update mongo
    def addWorkshopU(self, ws):
        #wgL = self.getWorkshopGroupList()
        self.workshopUnitList = self.workshopUnitList + ws
        # update mongo

    def deleteWorkhsopG(self,ws):
        self.workshopGoupList.remove(ws)
        #update mongo
    def deleteWorkshopU(self,ws):
        self.workshopUnitList.remove(ws)

    def getWorkshopGroupList(self):
        return self.workshopGoupList
    def getWorkshopUnitList(self):
        return self.workshopUnitList

    def cloneWG(self,name,numCopys,vrdp,netAdapter):
        clonedWG=[]
        wgList=self.getWorkshopGroupList()
        for wg in wgList:
            #print wg.name
            if wg.name== name:
                clonedWG=wg.cloneWorkshop(name,numCopys,vrdp,netAdapter)
        self.addWorkshopG(clonedWG)

    def cloneWU(self,name,numCopys,vrdp,netAdapter):
        clonedWU=[]
        wuList=self.getWorkshopUnitList()
        for wu in wuList:
            if wu.name== name:
                clonedWU=wu.cloneWorkshop(name,numCopys,vrdp,netAdapter)
        self.addWorkshopU(clonedWU)

    def groupVM(self,name,group):
        subprocess.check_output(["C:\Program Files\Oracle\VirtualBox\VBoxManage.exe", "modifyvm", name, "--groups", "/"+group])

    def getWorkshopGroup(self,name):
        wgList=self.getWorkshopGroupList()
        for wg in wgList:
            if wg.name== name:
                return wg

    def getWorkshopUnit(self,name):
        wuList=self.getWorkshopUnitList()
        for wu in wuList:
            if wu.name== name:
                return wu

