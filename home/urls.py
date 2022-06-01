from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("clock",views.stop_watch,name='home'),
    path("timer",views.timer,name='home')
]
