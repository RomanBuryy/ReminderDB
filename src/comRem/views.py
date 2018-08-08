from django.shortcuts import render

from django.views.generic import ListView
from .models import Comand



# Create your views here.

class HomePageView(ListView):
    model = Comand
    template_name = 'home.html'
