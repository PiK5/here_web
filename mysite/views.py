from django.shortcuts import render
from django import forms
import os


def index(request):
    return render(request,'index.html')

def route_map(request):
    if 'xy' in request.POST:
        coor = request.POST['xy']
        b = coor.find("Long:")
        lat = coor[5:b]
        long = coor[b+6::]      
    return render(request,'route_map.html',{'lat': lat, 'lon': long})

def road_time(request):
    if 'xy' in request.POST:
        coor = request.POST['xy']
        b = coor.find("Long:")
        lat = coor[5:b]
        long = coor[b+6::]      
    return render(request,'road_time.html',{'lat': lat, 'lon': long})

def POI(request):
    if 'xy' in request.POST:
        coor = request.POST['xy']
        b = coor.find("Long:")
        lat = coor[5:b]
        long = coor[b+6::]      
    return render(request,'POI.html',{'lat': lat, 'lon': long})

