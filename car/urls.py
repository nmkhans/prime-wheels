from django.urls import path
from . import views

urlpatterns = [
  path('add/', views.CarAddView.as_view(), name = 'car-add'),
  path('<slug:slug_name>/', views.car_detail, name = 'car-detail'),
]
