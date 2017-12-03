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

    def createGroup(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,units):
        wgList=self.getWorkshopGroupList()
        for wrkshpG in  wgList:
            if wrkshpG.name == name:
                return "Workshop group name is not unique"
        newWg= workshopGroup(name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,units)
        self.addWorkshop(newWg,wgList)
        #update database
    def createUnit(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,vm):
        wuList=self.getWorkshopUnitList()
        for wrkshpU in  wuList:
            if wrkshpU.name == name:
                return "Workshop unit name is not unique"
        newWu=workshopUnit(name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,vm)
        self.addWorkshop(newWu,wuList)
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

