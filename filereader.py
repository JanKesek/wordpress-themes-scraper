from os import listdir, remove
from os.path import isfile, join
class Reader:
    def __init__(self, path):
        self.path=path
    def getFiles(self):
        return [f for f in listdir(self.path) if isfile(join(self.path,f))]
    def getFileText(self,filename):
        f=open("testDir/"+filename, "r", encoding = "ISO-8859-1")
        return f.read()
    def deleteFile(self, filename):
        remove(self.path+"/"+filename)
    def writeToFile(self, filename, text):
        f=open("testDir/"+filename, "w")
        f.write(text)
