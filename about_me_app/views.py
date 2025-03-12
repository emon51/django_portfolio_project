from django.shortcuts import render, HttpResponse
from . models import About
# Create your views here.

def home(request):
    return render(request, 'html/home.html')

def about(request):
    objects = About.objects.get(id = 1)
    return render(request, 'html/about_me.html', context = {'objects': objects})

def education(request):
    objects = About.objects.get(id = 1)
    return render(request, 'html/education.html', context = {'objects': objects})

def contact(request):
    objects = About.objects.get(id = 1)
    return render(request, 'html/contact.html', context = {'objects': objects})