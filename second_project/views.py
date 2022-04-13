
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course


def index(request):
    course = Course.objects.all()
    return render(request, 'index.html', {'course': course})


def new(request):
    return HttpResponse('New Course')
