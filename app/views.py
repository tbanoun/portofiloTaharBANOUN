from django.shortcuts import render
from app.models import Projet

# Create your views here.

def hello(self):
    return render(self,'app/tahar.html')


def test(self):
    return render(self,'app/nav_bar.html')