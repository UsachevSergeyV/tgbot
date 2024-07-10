import requests
import parsingXML
import uuid
import urllib3
from datetime import datetime, timezone
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
endpoint = "https://int44.zakupki.gov.ru/eis-integration/services/getDocsMis2"

def getContract(reestrNumber):
    createTime = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    body=u"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://zakupki.gov.ru/fz44/get-docs-mis/ws">
    <soapenv:Header/>
    <soapenv:Body>
      <ws:getPublicDocsByReestrNumberRequest>
         <index>
         <id>{id}</id>
            <sender>test_005</sender>
            <createDateTime>2024-07-05T09:45:47Z</createDateTime>
            <mode>PROD</mode>
         </index>
         <selectionParams44>
            <subsystemType>RGK</subsystemType>
             <reestrNumber>{reestrNumber}</reestrNumber>
            <isAllOrganizations44>true</isAllOrganizations44>
         </selectionParams44>
      </ws:getPublicDocsByReestrNumberRequest>
    </soapenv:Body>
    </soapenv:Envelope>""".format(id=uuid.uuid4(),reestrNumber=reestrNumber)
    body = body.encode('utf-8')
    session = requests.session()
    session.headers = {"Content-Type": "text/xml; charset=utf-8"}
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    session.get(endpoint, verify=False)
    response = session.post(url=endpoint, data=body, verify=False)
    content = response.content.decode('utf-8')
    arrayUrl = parsingXML.getArrayUrlArchive(content)
    return  arrayUrl
