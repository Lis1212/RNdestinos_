from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, mundo! Esta é minha índice de enquetes")

# Create your views here.
