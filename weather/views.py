import requests
from django.shortcuts import render, redirect
from . models import City
from . forms import CityForm

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=ccc3992728385e710009902808f28b61'

    err_msg = ''
    message = ''
    message_class = ''

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()
            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                # print(r)
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'City does not exists in the world!'
            else:
                err_msg = 'City already exists in the Database!'

        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'City Added Successfully'
            message_class = 'is-success'

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

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
        weather_data.append(city_weather)

    params = {
            'weather_data': weather_data,
            'form': form,
            'message': message,
            'message_class': message_class,
            }

    return render(request, 'weather/index.html', params)


def delete_city(request, city_name):
    City.objects.get(name=city_name).delete()
    return redirect('Home')