from django.shortcuts import render
from brand.models import Brand

def home(req):
  brands = Brand.objects.all()
  return render(req, 'index.html', {'brands': brands})