from django.shortcuts import render
from django.http import HttpResponse
import string
import random

# Create your views here.

def home(request):
	return render(request, 'generator/home.html')

def password(request):

	thepassword = ''

	characters = list('abcdefghijklmnopqrstuvwxyz')

	length = int(request.GET.get('length', 12))

	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('numbers'):
		characters.extend(list('1234567890'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&*()'))

	for x in range(length):
		if x == 0 and not request.GET.get('uppercase'):
			thepassword += random.choice(string.ascii_lowercase)
		elif x == 0:
			thepassword += random.choice(string.ascii_letters)
		else:
			thepassword += random.choice(characters)


	return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
	return render(request, 'generator/about.html')