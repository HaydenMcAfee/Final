from django.shortcuts import render
import urllib
from urllib import request
from datetime import datetime
import json
from application.models import Course


def home_page(request):
    return render(request, 'application/index.html')

def hw2_page(request):
    return render(request, 'application/hw2.html')

def hw5_page(request):
    user_apiid = '75ea7649bb35dbd94c39e201d2f0a037'
    source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?zip=23666,us&appid=75ea7649bb35dbd94c39e201d2f0a037&units=imperial' +str(user_apiid) +'&units=imperial').read()

    data = json.loads(source)
    weather = {
        'city' : data['name'],
        'temp' : data['main']['temp'],
        'pres' : data['main']['pressure'],
        'windspd' : data['wind']['speed'],
        'winddir' : data['wind']['deg'],
        'now' : datetime.now(), # time object
        'name' : 'Hayden'
    }
    return render(request, 'application/hw5.html', {'weather': weather})

def final_page(request):
    course = Course.objects.all().order_by('course_id')

    return render(request, 'application/final.html', {'course': course})
