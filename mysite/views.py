from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from mysite.models import TrafficAccident

# Create your views here.
def index(request):
    return render(request,'index.html',locals())


def trafficData(request):
    A1 = TrafficAccident.objects.filter(accidentLevel__contains='A1').count()
    A2 = TrafficAccident.objects.filter(accidentLevel__contains='A2').count()
    A3 = TrafficAccident.objects.filter(accidentLevel__contains='A3').count()
    accidentLevel = {
        "A1":A1,
        "A2":A2,
        "A3":A3,
    }
    return render(request,'trafficData.html',locals())

def get_accident_level(request,id,*args,**kwargs,):
    yearMonth = id
    print(id)
    A1 = TrafficAccident.objects.filter(Q(accidentLevel__contains = 'A1') & Q(yearMonth__contains = yearMonth)).count()
    A2 = TrafficAccident.objects.filter(Q(accidentLevel__contains = 'A2') & Q(yearMonth__contains = yearMonth)).count()
    A3 = TrafficAccident.objects.filter(Q(accidentLevel__contains = 'A3') & Q(yearMonth__contains = yearMonth)).count()
    accidentLevel = {
        "A1":A1,
        "A2":A2,
        "A3":A3,
    }


    return JsonResponse(accidentLevel,safe='false')
    # return render(request,'trafficData.html',locals())