from django.contrib import admin
from django.urls import path, include

from calculaterapp import views

urlpatterns = [

    path('',views.home,name='home'),
    path('calc/',views.calc,name='calc')
]
