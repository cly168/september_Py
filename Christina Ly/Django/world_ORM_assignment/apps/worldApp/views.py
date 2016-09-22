from django.shortcuts import render
from . import models
from django.db.models import Count
# Create your views here.
def one(req):
    cities = models.Countries.objects.filter(languagetocountry__language='slovene')
    languages = models.Languages.objects.filter(language='slovene').order_by('percentage')
    return render(req, 'worldApp/index.html', context={'languages':languages})
def two(request):
	countries= models.Countries.objects.annotate(city_count = Count('citytocountry')).order_by('-city_count')
	for country in countries:
		print country.code
		print country.city_count
	return render(request, 'worldApp/index.html')
def three(request):
	cities = models.Cities.objects.filter(country__name = "Mexico").filter(population__gt = 500000).order_by('-population')
	for city in cities:
		print city.name
	return render(request, 'worldApp/index.html')
