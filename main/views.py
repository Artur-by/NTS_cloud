import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import *
from .forms import *


# Create your views here.

def course(code):
    url = f'https://www.nbrb.by/api/exrates/rates/{code}'
    response = requests.get(url).json()
    valuta = response['Cur_Name'] + ' ' + str(response['Cur_OfficialRate'])
    return valuta

def startPage(request):
    usd = course('145')
    euro = course('292')
    rub = course('298')
    if request.method == "POST":
        unp = request.POST.get('УНП')
        login = request.POST.get("Пользователь")
        password = request.POST.get("Пароль")
        return HttpResponse(f"<p>Привет {login} , добро пожаловать на вечеринку!</p>")
    else:

        form = userForms()
        return render(request,  'start.html', {'form': form, "euro": euro, 'usd': usd, 'rub': rub})






