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
from mysite.views import index, trafficData_109, trafficData_110, get_accident_level, trafficMap, get_accident_trafficMap,home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('trafficData_109/',trafficData_109),
    path('trafficData_110/',trafficData_110),
    path('trafficMap/',trafficMap),
    path('api/data/get_accident_level/<int:id>/',get_accident_level , name="api-data"),
    path('api/data/get_accident_trafficMap/<int:yearMonth>/<int:level>/',get_accident_trafficMap , name="api-data-2"),

    path('home/',home),
]
