from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nike', views.nike, name='nike'),
    path('parking', views.parking, name='parking'),
    path('milk', views.milk, name='milk'),
    path('money', views.money, name='money'),
]