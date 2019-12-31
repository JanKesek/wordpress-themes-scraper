import filereader
import lowercaser


reader = filereader.Reader("testDir")
listOfFiles=reader.getFiles()
l=lowercaser.Lowercaser()

for fileName in listOfFiles:
    text=reader.getFileText(fileName)
    textDic = {fileName:[text]}
    l.add(textDic)
for fileName in listOfFiles:
    lowerCaseText=l.convert(fileName)
    reader.writeToFile(fileName, lowerCaseText)
