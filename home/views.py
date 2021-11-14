from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .models import Hotel

# Create your views here.
def web_scraper():
     import requests
     from bs4 import BeautifulSoup

     URL = "https://www-swiggy-com.cdn.ampproject.org/c/s/www.swiggy.com/kollam"
     page = requests.get(URL)

     soup = BeautifulSoup(page.content, "html.parser")
     table = soup.findAll('div', attrs = {'class':'_3hrn8'}) 
     hotel_list =[]
     for row in table:
         hotel = {}
         hotel['link'] = row.find('a', {'class':'nYpnP','href':True}) ['href']
         hotel['image'] = row.find("amp-img")['src']
         hotel['name'] = row.find('div', attrs = {'class':'_3yTMU'}).text
         hotel['title'] = row.find('div', attrs = {'class':'_2tK-y'}).text
         for starAndCost in row.findAll('div', attrs = {'class':'_34od4'}):
            hotel['star'] = starAndCost.find('div',attrs
            = {'class':'Lbhht'}).text
            hotel['costOfTwo'] = starAndCost.find('div',attrs= {'class':'_3NRFO'}).text
         
         hotel_list.append(hotel)
     return hotel_list
@login_required
def index(request):
    #hotels = Hotel.objects.all()
    hotels= web_scraper()
    return render(request,'home.html',{'hotels':hotels})