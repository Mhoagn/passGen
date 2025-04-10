from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello World,</h1> This is my first Django Project')

def passGen(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    password = ""
    for i in range(15):
        ch = random.choice(characters)
        password += ch
    pas = {'password':password}
    return JsonResponse(pas)