import logging
import requests
import urllib
import time
import uuid
def getFile(arrayUrl):
    fileForRet = []
    for url in arrayUrl:
        fileName = "tempArh/f_" + str(uuid.uuid4())+".zip"
        for i in range(1, 26):
            if requests.get(url).status_code==200: #urllib.request.urlopen(url).getcode() == 200:
                break
            else:
                print("файл не найден, ждемс ["+str(i)+"]")
                time.sleep(1)
            if(i==25):
                {
                    print("файл не повился")
                }
                return []
        urllib.request.urlretrieve(url, fileName)
        print("файл найден")
        fileForRet.append(fileName)
    return fileForRet

