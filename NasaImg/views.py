from django.shortcuts import render
import requests as rq
import json

def home_view(request):
    context = {}
    return render(request, "Main.html", context)

def image_view(request):
    context = {}
    return render(request, "Main.html", context)

def image_day_view(request):
    context = Get_Img_nasa()
    print(context)
    return render(request, "imgday.html", context)

def Get_Img_nasa():
    ret = rq.get("https://api.nasa.gov/planetary/apod?api_key=DVejQ1l5jOwFbFJhafaTQbInVB8rp6inonHtn4mN",)
    jsonRet = json.loads(ret.content.decode('utf-8'))
    #for x in jsonRet:
       #print(jsonRet[x])
    return jsonRet
