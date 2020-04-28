import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ccc3992728385e710009902808f28b61'
    city = 'Vadodara'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': int(r['main']['temp']) - 273,
        'description': r['weather'][0]['description'] ,
        'max-temp': r['main']['temp_max'] ,
        'min-temp': r['main']['temp_min'] ,
        'icon': r['weather'][0]['icon'],
        'humidity': r['main']['humidity'],
    }
    print(city_weather)
    return render(request, 'weather/index.html', city_weather)