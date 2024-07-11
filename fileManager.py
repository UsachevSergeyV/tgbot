import logging
import zipfile
import os
def Summon_Mr_Proper(arrFile):
    for af in arrFile:
        os.remove(path=af)
    logging.warning("выданные файлы удалены");

def killSig(arrFile):
    for i in range(0,len(arrFile)):
        zin = zipfile.ZipFile(arrFile[i], 'r')
        newname = arrFile[i].replace('.zip','_withoutSig.zip')
        zout = zipfile.ZipFile(newname, 'w')
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if (item.filename[-4:] != '.sig'):
                zout.writestr(item, buffer)
        zout.close()
        zin.close()
        os.remove(path=arrFile[i])
        arrFile[i]=newname
    return arrFile
