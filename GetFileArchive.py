import logging

import requests
import  urllib
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
                logging.warning("файл не найден, ждемс ["+str(i)+"]")
                time.sleep(1)
            if(i==25):
                {
                    logging.WARNING("файл не повился")
                }
                return []
        urllib.request.urlretrieve(url, fileName)
        logging.warning("файл найден")
        fileForRet.append(fileName)
    return fileForRet






#//rc = []
#//ar = ['https://int44.zakupki.gov.ru/dstore/mis2/download/file.zip?ticket=bFMRlD%2BuSzrZjOv0PyWoWBweLdKA1xIQ0gqVMI8dEVAJ1KTvFw%2FNYGBQfb2Wgs6wFKeAlDY5mouy0mIFBu2Yf3pTeK2ecHevAfPPGXvDscBT6xg%2B67ZPjPnY%2F6RB%2BWxhOl8Xdbl3FC4BhkrSV%2FYGzLXFeGDcsK0gOE7C0KlOiqV8ROomFWNkya2oTydONo48gPjMbGN939aXaQqs5c8OZWzvanpYKhopgH1eYBzmh577suj22%2B5I4J6M3hqQ9j1CsbFG3JPFWLKmxeEw5Fuwo5XXg4Jo6hoSZRM7GQPraXR2MDlunBsSFug2Ecy3sYeg1eSFK4KuGFOVFX33A9GnJw%3D%3D', 'https://int44.zakupki.gov.ru/dstore/mis2/download/file.zip?ticket=j3poLEDb4o1fnNUaMh1ThxJEZC6%2FHch0mk5s5CTuSCiATbql%2B3GqSDkRzqZ6Ne%2BlPZNHTXIXx7wq%2BgtrU8BaKyN5yqScU%2BYlMMJABMk%2BqpSNaNy9vnNRSrCuststWlInQG%2Bb0JWvO3s2HiUPAqqHS3QtoHc9uZFmwt7WQzujgx7wmIYv5i6TphrW0hXdsrza0GBGc1v3lKCUC8nrWkwkxNh5aWrNLwhK6qdILvT8V2%2F7N0MXnCaTO4ald2ARL4P2iWd3Uujo%2BXahn99UrfOWBcu7TCfE2pE9edyAdbdlomsD%2FMCP%2BKVHDf9Ip%2FkzEtMpV1RVq25kkD2urn8uXIuHFw%3D%3D', 'https://int44.zakupki.gov.ru/dstore/mis2/download/file.zip?ticket=j2qKy3MSXuMGxx6vREAm46XSafD1AhWClW6%2FxIsIsKSo7eK5I3E9Gid8PJZA3Gvbe3XGILde9i5EB4RCyguilnmGXsDNv7F874IrcCpyi5kUT46fANirfVNVUZ34O%2FLTtpT6%2FuK9zOZUhmAyNtIvAzU0Lg2Ui3hitfWC%2FYru%2BACfjEa0BL6B6ssMlea7TKi1ODdoZXcl4XMxyC6XrCqsggyXUM8HNnkcZwOYVpTEXM3F%2BgFrnlQiD87EDarAA9RHMxWoaTlz0qWLLe2Sqa%2B2cQJbJIRm2A9Ey9e1DP1DcDc%2BvDKXAGPahGDI61cNAVcErg9vqoBKSIuhq5AO9Ci5WQ%3D%3D', 'https://int44.zakupki.gov.ru/dstore/mis2/download/file.zip?ticket=R9Gm3IJUYpUn95jk23nOsHbirHNCZ12Tre9hB63GIogGKuzVoCsO6Gpu8IRZnghqo2%2FMgoCCF8Fm9L%2BbG31dpKbe3BTi2jzZEvFsMQSK8d0n3D315M7L%2B7IvidCMCyXwVwXwW75dIM53zRk2ccLLUR%2BxxwxR5XF%2BzxlUgy6iMXqC74JHdnU5ISd%2BX3VI7xgqyzKobbvmqOn8CCgwC8A0X9bxy%2FGCy5Fwu%2BcC%2FbVA46wxMC257ncwIkPBrgDmRH3vxi9RaHIpE44xgCl0%2FptqoqiF4aExwDJ%2F1gci0vMNszJ4d4xrPorVgOmiXnYiVL8DeNkVrJ1I3ECLJZoIUD9Cbg%3D%3D']
#//getFile(ar)