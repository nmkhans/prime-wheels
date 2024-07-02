from django.shortcuts import render
from .models import Car

# Create your views here.
def car_detail(req, slug_name):
  car = Car.objects.get(slug = slug_name)
  return render(req, 'car/car_detail.html', {
    'car': car
  })