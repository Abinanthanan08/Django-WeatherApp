from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=81fffdda8ca86903c0c72be21729a2fb').read()
        json_data = json.loads(res)
        weather_data = {
            "temperature" : str(json_data['main']['temp']),
            "pressure" :str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
            "wind" : str(json_data['wind']['speed']),
            }
    else:
        city = ''
        weather_data = {}
    
    return render(request,'index.html',{'city':city,'weather_data':weather_data})
