import logging
import uuid
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
def killSigAndAddToOneZIP(arrFile, name, regnumb):
    newname = "tempArh/" + name +"_"+str(uuid.uuid4())+ "_withoutSIG.zip"
    kinds = {}
    zout = zipfile.ZipFile(newname, 'w')
    for i in range(0,len(arrFile)):
        zin = zipfile.ZipFile(arrFile[i], 'r')
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if (item.filename[-4:] != '.sig'):
                tmpkind = item.filename.split("_")[0]
                if tmpkind not in kinds:
                    kinds[tmpkind] = 1
                else:
                    kinds[tmpkind] += 1
                item.filename = tmpkind+"_"+regnumb+"_"+str(kinds[tmpkind])+".zip"
                zout.writestr(item, buffer)

        zin.close()
        os.remove(path=arrFile[i])
    zout.close()
    return newname,list(kinds.keys())

def getNameFileConcretKind(sysUser):

    if os.path.exists(str(sysUser["Path"])):
        nameNewFile = str(sysUser["Path"]).split('/')[0]+"/"+str(sysUser["RegNumber"])+"_"+str(sysUser["Kind"])+".zip"
        zout = zipfile.ZipFile(nameNewFile, 'w')
        zin = zipfile.ZipFile(str(sysUser["Path"]), 'r')
        for item in zin.infolist():
            buffer = zin.read(item.filename)
            if (str(item.filename).startswith(str(sysUser["Kind"]))):
                zout.writestr(item, buffer)
        zin.close()
        zout.close()
        return nameNewFile
    else:
        return None