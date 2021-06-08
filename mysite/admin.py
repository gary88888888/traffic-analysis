from django.contrib import admin
from mysite.models import TrafficAccident
# from mysite.models import TrafficAccident_110
class TrafficAccidentAdmin(admin.ModelAdmin):#客製化後台管理介面的標頭
    list_display = ('accidentID', 'yearMonth', 'processingUnit', 'accidentLevel', 'accidentTime', 'dist', 'streetRoad', 'roadclass', 'roadType', 'light', 'accidentType', 'whether', 'deathNum', 'injuryNum', 'roadStatus', 'roadDefect', 'speedLimit', 'obstacle', 'positionX', 'positionY')









# Register your models here.
admin.site.register(TrafficAccident, TrafficAccidentAdmin)
