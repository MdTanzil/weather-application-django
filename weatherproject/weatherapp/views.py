from django.shortcuts import render
from django.views.generic import TemplateView
import requests
# Create your views here.
def index(request):
    return render(request , 'weatherapp/home.html')


class HomePageView(TemplateView):
    template_name = "weatherapp/Home.html"
    url ="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6d3cb2fa8abd45a6e8ef13ed0b4b60ef"
    city= "Pakistan"
    r = requests.get(url.format(city)).json()

    city_weather = {
            'city' : 'Dhaka',
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
    print(city_weather)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_weather'] = self.city_weather
        return context
    
