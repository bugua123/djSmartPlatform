import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse

from .models  import  *
# Create your views here.
def index(request):
    # context=loadinfo()
    context={}
    return render(request, 'index.html', context=context)


