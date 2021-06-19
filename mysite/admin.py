from django.contrib import admin
from mysite.models import TrafficAccident,SpeedMeasuring

from import_export.admin import ImportExportModelAdmin
# from mysite.models import TrafficAccident_110
class TrafficAccidentAdmin(ImportExportModelAdmin):#客製化後台管理介面的標頭
    list_display = ('accidentID', 'yearMonth', 'processingUnit', 'accidentLevel', 'accidentTime', 'dist', 'streetRoad', 'roadclass', 'roadType', 'light', 'accidentType', 'weather', 'deathNum', 'injuryNum', 'roadStatus', 'roadDefect', 'speedLimit', 'obstacle', 'positionX', 'positionY')



class SpeedMeasuringAdmin(ImportExportModelAdmin):#客製化後台管理介面的標頭
    list_display = ('cameraID', 'cameraType', 'location', 'direction', 'limit', 'dist', 'ViolationType', 'positionX', 'positionY')





# Register your models here.
admin.site.register(TrafficAccident, TrafficAccidentAdmin)
admin.site.register(SpeedMeasuring, SpeedMeasuringAdmin)


