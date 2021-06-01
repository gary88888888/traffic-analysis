import os
import django
import requests as rq
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "datacenter.settings")
django.setup()

from mysite.models import TrafficAccident

url ="https://api.kcg.gov.tw/api/service/get/c0bbdc36-444e-48b4-a42c-85ae074edfac"
rawdata = rq.get(url)
# json_dict = json.loads(resp.text)
data = rawdata.json()["data"]
# print(data)


for d in data:

    newData = TrafficAccident(yearMonth = d["事故年月"],processingUnit = d["單位名稱"],accidentLevel = d["事故類別"],accidentTime = d["發生日期"],dist = d["鄉鎮市區"],streetRoad = d["街路"],roadclass = d["道路說明"],roadType = d["道路型態說明"],light = d["光線說明"],accidentType = d["事故類型及型態說明"],whether = d["天候說明"],deathNum = d["死亡人數"],injuryNum = d["受傷人數"],roadStatus = d["路面狀態說明"],roadDefect = d["路面缺陷說明"],speedLimit = d["速限"],obstacle = d["障礙物說明"],positionX = d["x"],positionY = d["y"])

    newData.save()
    # newData = d["事故年月"]
    # print(newData)