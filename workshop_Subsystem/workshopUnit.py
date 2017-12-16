import workshop from workshop
class workshopUnit:
    def __init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,vm):
        workshop.__init__(name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial)
        self.vm=vm
    def vmStatus(self):

    def getPersistenceState(self):

    def getSessionState(self):
    
