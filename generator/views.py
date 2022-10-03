from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    # return HttpResponse("Hello there friend!")
    return render(request, 'generator/home.html')

def password(request):

    length = int(request.GET.get('length'), 12)
    alefBet = 'abcdefghijklmnopqrstuvwxwz'
    characters = list(alefBet)
    specialCharacters = '~!@#$%^&*()-_+=[{}]|,<.>/?'
    digits = '0123456789'

    # If uppercase is set, extend character list
    if request.GET.get('uppercase'):
        characters.extend(list(alefBet.upper()))

    # Also, for special
    if request.GET.get('special'):
        characters.extend(list(specialCharacters))

    # Also, for numbers (actually, for digits)
    if request.GET.get('numbers'):
        characters.extend(list(digits))


    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password})
