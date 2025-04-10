from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    return render(request,'home.html')

def passGen(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    password = ""

   
    length = request.GET.get('length')
    special_chars = request.GET.get('special_chars')  # "on" hoặc None
    uppercase = request.GET.get('uppercase')
    havingDigits = request.GET.get('havingDigits')

    # Chuyển length sang int
    try:
        length = int(length)
    except (TypeError, ValueError):
        length = 0  # xử lý nếu không hợp lệ

    
    if uppercase == "on":
        characters += list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if special_chars == "on":
        characters += list('!@#$%^&*()-_=+[]{};:,.<>?/')
    if havingDigits == "on":
        characters += list('0123456789')

   
    if length > 0:
        password = ''.join(random.choice(characters) for _ in range(length))
    else:
        password = "Độ dài không hợp lệ!"

    return render(request, 'password.html', {'password': password})
