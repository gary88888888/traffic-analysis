from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from mysite.models import TrafficAccident,SpeedMeasuring
@csrf_exempt
# Create your views here.
def index(request):
    return render(request,'index.html',locals())

def accident_count(request):
    return render(request,'accident_count.html',locals())

def home(request):
    return render(request,'home.html',locals())

def trafficData_109(request):
    A1 = TrafficAccident.objects.filter(accidentLevel__contains='A1').count()
    A2 = TrafficAccident.objects.filter(accidentLevel__contains='A2').count()
    A3 = TrafficAccident.objects.filter(accidentLevel__contains='A3').count()
    accidentLevel = {
        "A1":A1,
        "A2":A2,
        "A3":A3,
    }
    return render(request,'trafficData_109.html',locals())


def trafficData_110(request):
    A1 = TrafficAccident.objects.filter(accidentLevel__contains='A1').count()
    A2 = TrafficAccident.objects.filter(accidentLevel__contains='A2').count()
    A3 = TrafficAccident.objects.filter(accidentLevel__contains='A3').count()
    accidentLevel = {
        "A1":A1,
        "A2":A2,
        "A3":A3,
    }
    return render(request,'trafficData_110.html',locals())

def trafficMap(request):
    return render(request,'trafficMap.html',locals())
def accident_type(request):
    return render(request,'accident_type_chart.html',locals())










##--------------API---------------------

def accident_count_data(request):
    if request.method == 'POST':
        level = request.POST.get("level")

    A1t = TrafficAccident.objects.filter(accidentLevel__contains= level )


    A1 = serializers.serialize("json", A1t,ensure_ascii=False )

    return HttpResponse(A1, content_type='application/json; charset=utf-8')


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



def get_accident_trafficMap_yearMonth(request,yearMonth,*args,**kwargs,):
    yearMonth = yearMonth


    data =  serializers.serialize("json", TrafficAccident.objects.filter( Q(yearMonth__contains = yearMonth) ),ensure_ascii=False )
    return HttpResponse(data, content_type='application/json; charset=utf-8')
def get_accident_trafficMap_yearMonth_level(request,yearMonth,level,*args,**kwargs,):
    yearMonth = yearMonth
    level = level


    data =  serializers.serialize("json", TrafficAccident.objects.filter( Q(yearMonth__contains = yearMonth) & Q(accidentLevel__contains = level)),ensure_ascii=False )
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def get_accident_trafficMap(request,*args,**kwargs,):
    if request.method == 'POST':
        yearMonth = request.POST.get("yearMonth")
        level = request.POST.get("level")
        weather = request.POST.get("weather")

    data =  serializers.serialize("json", TrafficAccident.objects.filter(Q(accidentLevel__contains = level) & Q(yearMonth__contains = yearMonth)  & Q(weather__contains = weather)),ensure_ascii=False )

    return HttpResponse(data, content_type='application/json; charset=utf-8')

def get_accident_camera(request,*args,**kwargs,):



    data =  serializers.serialize("json", SpeedMeasuring.objects.all(),ensure_ascii=False )
    return HttpResponse(data, content_type='application/json; charset=utf-8')

def get_accident_type(request,*args,**kwargs,):

    chase = TrafficAccident.objects.filter(Q(accidentType__contains = '追撞')).count()
    Crossroads  = TrafficAccident.objects.filter(Q(accidentType__contains = '路口交岔撞')).count()
    Rollover  = TrafficAccident.objects.filter(Q(accidentType__contains = '路上翻車')).count()
    Traverse  = TrafficAccident.objects.filter(Q(accidentType__contains = '穿越道路中')).count()
    Hit_guardrail  = TrafficAccident.objects.filter(Q(accidentType__contains = '撞護欄')).count()
    Hit_sign  = TrafficAccident.objects.filter(Q(accidentType__contains = '撞號誌')).count()
    Hit_bridge = TrafficAccident.objects.filter(Q(accidentType__contains = '撞橋梁')).count()
    Hit_construction  = TrafficAccident.objects.filter(Q(accidentType__contains = '撞工程施工')).count()
    Hit_animal = TrafficAccident.objects.filter(Q(accidentType__contains = '撞動物')).count()
    Approach_road = TrafficAccident.objects.filter(Q(accidentType__contains = '接近路中')).count()
    Hit_Non_fixed_facilities  = TrafficAccident.objects.filter(Q(accidentType__contains = '撞非固定設施')).count()
    Collision  = TrafficAccident.objects.filter(Q(accidentType__contains = '對撞')).count()
    Opposite_traffic  = TrafficAccident.objects.filter(Q(accidentType__contains = '對向通行中')).count()
    Opposite_Scratch   = TrafficAccident.objects.filter(Q(accidentType__contains = '對向擦撞')).count()
    Scratch  = TrafficAccident.objects.filter(Q(accidentType__contains = '同向擦撞')).count()
    others = TrafficAccident.objects.filter(Q(accidentType__contains = '其他')).count()
    Side_collision  = TrafficAccident.objects.filter(Q(accidentType__contains = '側撞')).count()
    Stop_side = TrafficAccident.objects.filter(Q(accidentType__contains = '停立路邊')).count()
    Astern_hit = TrafficAccident.objects.filter(Q(accidentType__contains = '倒車撞')).count()
    Hit_tree = TrafficAccident.objects.filter(Q(accidentType__contains = '撞路樹')).count()
    Hit_Separate_island  = TrafficAccident.objects.filter(Q(accidentType__contains = '撞交通島')).count()

    data={
        'chase':chase,
        'Crossroads':Crossroads,
        'Rollover':Rollover,
        'Traverse':Traverse,
        'Hit_guardrail':Hit_guardrail,
        'Hit_sign':Hit_sign,
        'Hit_bridge':Hit_bridge,
        'Hit_construction':Hit_construction,
        'Hit_animal':Hit_animal,
        'Approach_road':Approach_road,
        'Hit_Non_fixed_facilities':Hit_Non_fixed_facilities,
        'Collision':Collision,
        'Opposite_traffic':Opposite_traffic,
        'Opposite_Scratch':Opposite_Scratch,
        'Scratch':Scratch,
        'Side_collision':Side_collision,
        'others':others,
        'Stop_side':Stop_side,
        'Astern_hit':Astern_hit,
        'Hit_tree':Hit_tree,
        'Hit_Separate_island':Hit_Separate_island,
    }




    return JsonResponse(data,safe='false')

