from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{
        'pasw':'lee'
    })
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    
    length=int(request.GET.get('length',7))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    password=''
    for x in range(length):
       password+=random.choice(characters)
    return render(request,'generator/password.html',{
        'pasw':password
    })
def about(request):
    return render(request,'generator/about.html')

