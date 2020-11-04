from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb
from django.template import loader

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'bboard/index.html', {'bbs':bbs})
