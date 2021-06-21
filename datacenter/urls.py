"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from mysite.views import get_accident_trafficMap,get_accident_trafficMap_yearMonth,get_accident_trafficMap_yearMonth_level
from mysite.views import  trafficData_109, trafficData_110, get_accident_level, trafficMap,accident_count,accident_count_data,get_accident_camera,home,about
from mysite.views import get_accident_type,accident_type



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/',home),
    path('about/',about),
    path('trafficData_109/',trafficData_109),
    path('trafficData_110/',trafficData_110),
    path('trafficMap/',trafficMap),
    path('accident_count/',accident_count),
    path('accident_type/',accident_type),



    path('api/data/get_accident_level/<int:id>/',get_accident_level , name="api-data"),
    path('api/data/get_accident_trafficMap/<int:yearMonth>/',get_accident_trafficMap_yearMonth , name="yearMonth"),
    path('api/data/get_accident_trafficMap/<int:yearMonth>/<int:level>/',get_accident_trafficMap_yearMonth_level , name="yearMonth_level"),
    path('api/data/get_accident_trafficMap/',get_accident_trafficMap , name="api-data-2"),
    path('api/data/get_accident_trafficMap/camera/',get_accident_camera , name="api-data-camera"),
    path('api/data/get_accident_count_datatestdata/',accident_count_data,name="get_accident_count_datatestdata"),
    path('api/data/get_accident_type/',get_accident_type,name="get_accident_type"),



]
