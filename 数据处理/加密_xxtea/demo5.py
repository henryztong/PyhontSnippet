# -*- coding:utf-8 -*-
import json
import urllib.parse
from hashlib import sha1


if __name__ == "__main__":
    jsonStr = '{"bankMblNo":"1571234567","socialIdentity":"1","qryCreditId":"1901310705017","oprMblNo":"15753760839","bankCardNo":"12345678901","userType":"01","usrJob":"001","requestTm":"20190710145800","zipCode":"370882","liveScore":"1","schooling":"003","creditTotScore":"3751","usrIdName":"name","applyIp":"127.0.0.1","companyName":"companyName","nation":"01","idCardBack":"22222222222222","country":"01","bankCode":"BCOM","contactName":"NAME","applyModelCode":"7548","creditModScore":"375","usrIdCard":"370882199312045826","jrnNo":"lb81420190701003","addressCode":"370800","contactMblNo":"1571234567","companyMblNo":"158123456","oprId":"OPR0001","livePicture":"1","companyAddress":"companyAddress","appId":"123","usrProvNo":"18","inCome":"9000","idCardFrontID":"1","idCardBackID":"1","idExpDt":"2050","hbScore":"375","contactRelation":"001","cusSex":"1","hbUsrNo":"4000705017","regDt":"20190215","idCardFront":"1111111111111111111","userStarLvl":"5","liveOrgNm":"1","userMail":"123@163.com","companyAddressCode":"123456","liveOrgId":"1","address":"address","mblNo":"15753760839","totalBonusAmt":"5000.0","bankCardName":"BANK_CARD_NAME","maritalSta":"1","livePictureID":"1"}'
    jsonDict = json.loads(jsonStr)
    print(type(jsonDict))



    jsonDictKeys = sorted(jsonDict.keys())
    # jsonDictKeys = sorted(jsonDict) #sorted默认取字典的键
    print(jsonDictKeys)
    string = ''
    for one in jsonDictKeys:
        string += one + jsonDict[one]
    codes = urllib.parse.quote(string)


    s1 = sha1()
    s1.update(codes.encode())
    sign = s1.hexdigest()




    print(sign)




    