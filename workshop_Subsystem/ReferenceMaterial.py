class ReferenceMaterial:
    def __init__(self,tag,filePath,fileType):
        self.tag=tag
        self.filePath=filePath
        self.fileType=fileType

    def setTag(self,newTag):
        self.tag=newTag
    def setFilePath(self,newFilePath):
        self.filePath=newFilePath
    def setFileType(self,newFileType):
        self.fileType=newFileType

    def getTag(self):
        return self.tag
    def getFilePath(self):
        return self.filePath
    def getFileType(self):
        return self.fileType
