#coding:utf-8
import os
import django
import requests as rq
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datacenter.settings")
django.setup()

from mysite.models import TrafficAccident

# lists = [
# "https://api.kcg.gov.tw/api/service/get/b97eb4a9-f6ac-43fc-ae19-6d54e626118a",#109-1
# "https://api.kcg.gov.tw/api/service/get/f5a4a10e-ccec-4e42-a59e-1eab80560922",#109-2
# "https://api.kcg.gov.tw/api/service/get/a2916482-989a-4365-9b46-76b744427c0f",#109-3
# "https://api.kcg.gov.tw/api/service/get/c0bbdc36-444e-48b4-a42c-85ae074edfac",#109-4
# "https://api.kcg.gov.tw/api/service/get/d32c8bcf-82b2-4061-92f8-0fe2efc29cd3",#109-5
# "https://api.kcg.gov.tw/api/service/get/5954c99d-8579-4521-971e-224033c52bfc",#109-6
# "https://api.kcg.gov.tw/api/service/get/3e092ef1-9a19-4e52-b567-eef48120147c",#109-7
# "https://api.kcg.gov.tw/api/service/get/69d586b4-88ab-40ba-82ab-1cec5acfa32f",#109-8
# "https://api.kcg.gov.tw/api/service/get/cd4519a2-a84c-411d-bad0-aee66e2f042d",#109-9
# "https://api.kcg.gov.tw/api/service/get/ad15de83-8642-4416-bfd1-be74fe8896e6",#109-10
# "https://api.kcg.gov.tw/api/service/get/186084ef-c11b-413e-81a6-e9cd3bc34f4f",#109-11
# "https://api.kcg.gov.tw/api/service/get/e930c74c-2ee1-4447-9596-5b67508e3259",#109-12
# "https://api.kcg.gov.tw/api/service/get/bb62ecd9-ca94-4e75-85d4-a9f019ad4c8d",#110-1
# "https://api.kcg.gov.tw/api/service/get/fc11bc7f-4e06-48cc-89b8-eea3ad8fdb29",#110-2
# "https://api.kcg.gov.tw/api/service/get/e3d8fff6-5704-4e10-8015-3f110a477f21"#110-3
# ]

url = "https://api.kcg.gov.tw/api/service/get/e3d8fff6-5704-4e10-8015-3f110a477f21"

rawdata = rq.get(url)
# json_dict = json.loads(resp.text)
data = rawdata.json()["data"]
# print(data)


for d in data:

    newData = TrafficAccident(yearMonth = d["事故年月"],processingUnit = d["單位名稱"],accidentLevel = d["事故類別"],accidentTime = d["發生日期"],dist = d["鄉鎮市區"],streetRoad = d["街路"],roadclass = d["道路說明"],roadType = d["道路型態說明"],light = d["光線說明"],accidentType = d["事故類型及型態說明"],whether = d["天候說明"],deathNum = d["死亡人數"],injuryNum = d["受傷人數"],roadStatus = d["路面狀態說明"],roadDefect = d["路面缺陷說明"],speedLimit = d["速限"],obstacle = d["障礙物說明"],positionX = d["x"],positionY = d["y"])

    newData.save()
    # newData = d["事故年月"]
    # print(newData)