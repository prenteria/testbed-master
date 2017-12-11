from Workshop import workshop
from workshopGroup import workshopGroup
from workshopUnit import workshopUnit
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
        self.addWorkshop(newWg,wgList)
        return newWg #delete
        #update database
    def createUnit(self,name,description,host,skillLevel,publishedDate,sessionType,vm):
        wuList=self.getWorkshopUnitList()
        for wrkshpU in  wuList:
            if wrkshpU.name == name:
                return "Workshop unit name is not unique"
        newWu=workshopUnit(name,description,host,skillLevel,publishedDate,sessionType,vm)
        self.addWorkshop(newWu,wuList)
        return newWu #delete
        #update mongo
        #create unit add to list update db
    def addWorkshop(self,ws,wsList):
        wsList.append(ws)
        #update mongo

    def deleteWorkhsop(self,ws,wsList):
        wsList.remove(ws)
        #update mongo

    def getWorkshopGroupList(self):
        return self.workshopGoupList
    def getWorkshopUnitList(self):
        return self.workshopUnitList

    def cloneWG(self,name,vrdp,netAdapter,numCopys):
        clonedWG=[]
        wgList=self.getWorkshopGroupList()
        for wg in wgList:
            if wg.name== name:
                clonedWG=wg.cloneWorkshop(name,numCopys,vrdp,netAdapter)
        self.addWorkshop(clonedWG,wgList)

    def cloneWU(self,name,vrdp,netAdapter,numCopys):
        clonedWU=[]
        wuList=self.getWorkshopUnitList()
        for wu in wuList:
            if wu.name== name:
                clonedWU=wu.cloneWorkshop(name,numCopys,vrdp,netAdapter)
        self.addWorkshop(clonedWU,wuList)

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

