from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from car.models import Car
from .models import Order
from django.contrib import messages

# Create your views here.
def place_order(req):
  username = req.GET.get('username')
  car_slug = req.GET.get('car')

  user = User.objects.get(username = username)
  car = Car.objects.get(slug = car_slug)

  if car.quantity > 0:
    car.quantity -= 1
    car.save()
    Order.objects.create(user = user, car = car)

    messages.success(req, 'Order placed.')
    return redirect('car-detail', slug_name = car.slug)
  else:
    messages.warning(req, 'No more car available on stock.')
    return redirect('car-detail', slug_name = car.slug)