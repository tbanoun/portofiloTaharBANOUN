from django.shortcuts import render
from app.models import Projet

# Create your views here.

def hello(self):
    pro = Projet.objects.all()
    return render(self,'app/mes_projets.html',{'pr':pro})


def test(self):
    return render(self,'app/nav_bar.html')