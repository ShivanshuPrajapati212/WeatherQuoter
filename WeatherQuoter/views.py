from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

key = "93b9a137b2944c45be5152042240305"

def getData(query):
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={query}&aqi=no"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = json.loads(soup.text)
    return data

def index(request):
    return render(request,'index.html')

def current(request):
    query = request.POST.get('query','India')
    try:
        results = getData(query)

        params = {
        "Location": results['location']['name'],
        "Time": results['location']['localtime'],
        "Temperature_in_Celsius": results['current']['temp_c'],
        "Temperature_in_Fahrenheit": results['current']['temp_f'],
        "Wind_Speed": results['current']['wind_kph'],
        "Humidity": results['current']['humidity'],
        "query": query,
        "url": f"https://api.weatherapi.com/v1/current.json?key={key}&q={query}&aqi=no"
    }
        return render(request, 'current.html',params)

    except:
        params = {
            'query': query
        }
        return render(request, 'error.html',params)

   