from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
import json
from requests import get
from bs4 import BeautifulSoup

# Create your views here.

def home(request):
    """exemple de vue avec Django"""
    return HttpResponse("""
    <h1>ma premiere vue en python evec Django</h1>
    <p>c'est mon premier paragraphe</p>
    """)


def scrap(request):
    url = 'https://www.matchendirect.fr/'
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')

    table = html_soup.find('div', attrs={'id': 'livescore'})
    compt = 1

    mydata = []

    for row in table.findAll('div', attrs={'class': 'panel panel-info'}):

        a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()

        for el in row.findAll('tr'):
            resultat = {}
            heure = el.find('td', attrs={'class': 'lm1'}).get_text()
            eqA = el.find('span', attrs={'class': 'lm3_eq1'}).get_text()
            eqB = el.find('span', attrs={'class': 'lm3_eq2'}).get_text()
            scors = el.find('span', attrs={'class': 'lm3_score'}).get_text()

            resultat['heure'] = heure
            resultat['eqa'] = eqA
            resultat['eqb'] = eqB
            resultat['scors'] = scors
            resultat['title'] = a_desc

            mydata.append(resultat)

    data = mydata

    # return JsonResponse(mydata, safe=False)  # retourn du json
    return render(request, 'parier/scrap.html', {'result': data})


def Home(request):
    return render(request, 'parier/home.html', {'date': datetime.now()})


