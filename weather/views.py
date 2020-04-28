import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ccc3992728385e710009902808f28b61'
    city = 'Vadodara'
    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'weather/index.html')