from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.index),
    path('products/create/', views.create),
    path('products/save/', views.save),
    path('products/edit/<id>/', views.edit),
    path('products/update/<id>/', views.update)
]