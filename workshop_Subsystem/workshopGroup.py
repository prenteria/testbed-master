from Workshop import workshop
import datetime
import workshopUnit
class workshopGroup(workshop):
    unitCount=0
    def __init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,units):
        self.units=[]
        workshop.__init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial)
        self.units=units

    def countUnits(self):
        index=0
        while index<len(self.units):
            unitCount=unitCount+1
        return unitCount
    def addUnit(self,workshopUnit):
        self.unit.append(workshopUnit)
    def setUnits(self,wu):
        self.units=wu
    def deleteWorkshop(self,workshopUnitName):
        self.unit.remove(workshopUnitName)
    def getUnitList(self):
        return self.units
    def cloneWorkshop(self,name,numClones,vrdpSeed,netAdptrSeed):
        index=0
        newUnits=[]
        while index < len(self.units):
            newUnits[index]=self.units[index].clone(name,numClones,vrdpSeed,netAdptrSeed)
            index=index+1
        newWorkshopGroup=workshopGroup(name,self.description,self.status,self.host,self.skillLevel,datetime.datetime.now(),self.sessionType,self.refMaterial,newUnits)
        return newWorkshopGroup

    def exportWorkshop(self, selectedWorkshopList):
        info=open(self.name+".txt","w+")
        info.write(self.name+"\n")
        info.write(self.description+"\n")
        info.write(self.status+"\n")
        info.write(self.host+"\n")
        info.write(self.skillLevel+"\n")
        info.write(self.publishedDate+"\n")
        info.write(self.sessionType+"\n")
        info.write (self.units+"\n")
        info.close()
        workshopUnit.exportWorkhop(self.units)
        #while index < len(self.units):
         #   newUnits[index] = self.units[index].clone(name, numClones, vrdpSeed, netAdptrSeed)
          #  index = index + 1
    def importWorkshop(self,name,description,rm,persistenceType,workshop,workshopList):
        info=open(name+".txt","r")
        workshop.setName(info.readline())
        workshop.setDescription(info.readline())
        workshop.setStatus(info.readline())
        workshop.setHost(info.readline())
        workshop.setSkillLevel(info.readline())
        workshop.setPublishedDate(info.readline())
        workshop.setSessionType(info.readline())
        workshopList.append(workshop)

        #n=info.readline()
        #desc=info.readline()
        #sts=info.readline()
        #hst=info.readline()
        #skll=info.readline()
        #pd=info.readline()
        #sesType=info.readline()
        #wsGroup=workshopGroup(n,desc,sts,hst,skll,pd,sesType,workshopUnit.importWorkshop())
        #workshopList.append(workshop)

        #workshop.setName(name)
        #workshop.setDescription(description)
        #workshop.setReferenceMatrial(rm)
        #workshop.setSessionType(persistenceType)
        #workshopList.append(workshop)

        info.close()
        workshopUnit.importWorkshop()
        return workshop