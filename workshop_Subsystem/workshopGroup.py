from workshop import Workshop
class workshopGroup(Workshop):
    def __init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial,units):
        Workshop.__init__(self,name,description,status,host,skillLevel,publishedDate,sessionType,refMaterial)
        self.units=units

    def countUnits(self):
    
