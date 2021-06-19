from django.db import models


class TrafficAccident(models.Model):

    accidentID = models.CharField(max_length=200)#案件編號
    yearMonth = models.CharField(max_length=200)#事故年月
    processingUnit = models.CharField(max_length=200)#單位名稱
    accidentLevel = models.CharField(max_length=200)#事故類別
    accidentTime = models.CharField(max_length=200)#發生日期
    dist = models.CharField(max_length=200)#鄉鎮市區
    streetRoad = models.CharField(max_length=200)#街路
    roadclass = models.CharField(max_length=200)#道路說明 ex.市區道路
    roadType = models.CharField(max_length=200)#道路型態說明    ex.直路 or 岔路
    light = models.CharField(max_length=200)#光線說明    ex.日間自然光線
    accidentType = models.CharField(max_length=200)#事故類型及型態說明    ex.側撞
    whether = models.CharField(max_length=200)#天候說明    ex.晴
    deathNum = models.CharField(max_length=200)#死亡人數    ex.1
    injuryNum = models.CharField(max_length=200)#受傷人數   ex.1
    roadStatus = models.CharField(max_length=200)#路面狀態說明    ex.乾燥
    roadDefect = models.CharField(max_length=200)#路面缺陷說明    ex.無缺陷
    speedLimit = models.CharField(max_length=200)#速限   ex.50
    obstacle = models.CharField(max_length=200)#障礙物說明   ex.無障礙物
    positionX = models.CharField(max_length=200)#x   ex.22.6810731
    positionY = models.CharField(max_length=200)#y   ex.120.3101755
    class Meta:
        ordering = ('-accidentTime',)

    def __str__(self):
        return self.accidentID


class SpeedMeasuring(models.Model):
    cameraID = models.CharField(max_length=20)#相機編號
    cameraType = models.CharField(max_length=20)#相機形式
    location = models.CharField(max_length=20)#相機位置
    direction = models.CharField(max_length=20)#測照方向
    limit = models.CharField(max_length=20)#速限或違規
    dist = models.CharField(max_length=20)#行政區
    ViolationType = models.CharField(max_length=20)#違規測照形式
    positionX = models.CharField(max_length=20)#相機編號
    positionY = models.CharField(max_length=20)#相機編號
    class Meta:
        ordering = ('-cameraID',)

    def __str__(self):
        return self.cameraID




# Create your models here.
