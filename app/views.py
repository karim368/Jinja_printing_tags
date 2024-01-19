from django.shortcuts import render

# Create your views here.
from datetime import date

def details(request):
    d = {'name':'Phatan Karim','age':23,'gender':'Male','status':'Single','date':date.today()}
    return render(request,'details.html',d)