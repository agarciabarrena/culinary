from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Test of the main page")

# Create your views here.
