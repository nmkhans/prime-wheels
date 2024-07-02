from django.shortcuts import render
from brand.models import Brand
from car.models import Car

def home(req):
  brands = Brand.objects.all()
  cars = Car.objects.all()
  return render(req, 'index.html', {
    'brands': brands,
    'cars': cars
  })