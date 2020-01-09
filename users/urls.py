
from django.contrib import admin
from django.urls import path

from users.views import aboutme, ziyu

app_name = 'users'

urlpatterns = [
    path('about', aboutme, name='aboutme'),
    path('ziyu', ziyu, name='ziyu'),

]
