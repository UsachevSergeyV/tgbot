import xml.etree.ElementTree as ET
fileXML = open('xmlTempl.xml')
xmlTest = fileXML.readline()
fileXML.close()
def getArrayUrlArchive(xmlData):
    tree = ET.fromstring(xmlData)
    arrayArhURL = tree.findall('.//archiveUrl')
    arrayUrl=[]
    for url in arrayArhURL:
        arrayUrl.append(url.text)
    return arrayUrl

#print(getArrayUrlArchive(xmlTest))