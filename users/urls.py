
from django.contrib import admin
from django.urls import path

from users.views import AuthView

app_name = 'users'

urlpatterns = [
    #path('api/v1/auth/', AuthView.as_view()),
]
