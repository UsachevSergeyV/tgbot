import xml.etree.ElementTree as ET

def getArrayUrlArchive(xmlData):
    tree = ET.fromstring(xmlData)
    arrayArhURL = tree.findall('.//archiveUrl')
    arrayUrl=[]
    for url in arrayArhURL:
        arrayUrl.append(url.text)
    return arrayUrl

