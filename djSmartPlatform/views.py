from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    # context=loadinfo()
    context={}
    return render(request, 'index.html', context=context)
