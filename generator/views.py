from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list(string.ascii_lowercase)
    length = int(request.GET.get('length',8))

    if request.GET.get('uppercase'):
        characters.extend(string.ascii_uppercase)
    if request.GET.get('special'):
        characters.extend(string.punctuation)
    if request.GET.get('numbers'):
        characters.extend(string.digits)

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password': thepassword })

# Create your views here.
