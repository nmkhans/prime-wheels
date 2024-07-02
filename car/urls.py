from django.urls import path
from . import views

urlpatterns = [
  path('<slug:slug_name>/', views.car_detail, name = 'car-detail')
]
