from django.shortcuts import render
from brand.models import Brand
from car.models import Car

def home(req, brand_slug = None):
  brands = Brand.objects.all()

  if brand_slug == None:
    cars = Car.objects.all()
  else:
    filtered_brand = Brand.objects.get(slug = brand_slug)
    cars = Car.objects.filter(brand = filtered_brand)

  return render(req, 'index.html', {
    'brands': brands,
    'cars': cars
  })