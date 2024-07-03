from django.urls import path
from . import views

urlpatterns = [
  path('add/', views.BrandAddView.as_view(), name = 'add-brand') 
]
