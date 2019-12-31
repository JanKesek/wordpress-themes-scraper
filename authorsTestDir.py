import filereader as f
import pickler
import re

obj=f.Reader("testDir2")

filesList=obj.getFiles()
p1=pickler.Pickler("listOfAuthorsWithoutEmpty")
originalDict=p1.retrieve()
#print(originalDict)
print(len(originalDict))

print(len(filesList))
t=[]
matchedFiles=[]
for f in filesList:
    txt=obj.getFileText(f)
    print(txt[0:1000])
    print("KOLEJNE")
    print("   |   ")
    print("   |   ")
    print("   |   ")
    print("   |   ")
    print(f)
    print("   |   ")
    print("   |   ")
    print("   |   ")
    print("   \/  ")
    #matched= re.findall(r" theme uri: http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+ ", txt)
    matched = re.findall(r"\s*author\s*:\s*http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+\s*$", txt, re.MULTILINE)
    if len(matched)!=0: 
        t.append(matched)
        originalDict[f]=matched
        matchedFiles.append(f)
for f in matchedFiles:
    obj.deleteFile(f)
print(t)
print(len(t))
print(len(originalDict))
#print(originalDict)
p2=pickler.Pickler("listOfAuthorsWithoutEmpty2")
p2.save(originalDict)
#print(t)
