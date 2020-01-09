from django.shortcuts import render
from .models import *
# Create your views here.
def aboutme(request):
    # context=loadinfo()
    context={}
    return render(request, 'about.html', context=context)
def ziyu(request):
    # context = loadinfo()
    context={}
    ziyu = Ziyu.objects.all()
    context['ziyu'] = ziyu
    return render(request, 'ziyu.html', context=context)