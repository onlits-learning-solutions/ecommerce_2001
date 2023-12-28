from django.urls import path
from . import views

urlpatterns = [
    path('sellers/', views.index),
    path('sellers/create/',views.create),
    path('sellers/save/',views.save)
]