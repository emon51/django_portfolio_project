from django.shortcuts import render, HttpResponse

from . models import Skills

# Create your views here.

def skill(request):
    objects = Skills.objects.get(id = 1)
    return render(request, 'html/skills.html', context = {'objects': objects})

def project(request):
    return render(request, 'html/project.html')