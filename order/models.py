from django.db import models
from django.contrib.auth.models import User
from car.models import Car

# Create your models here.
class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'order')
  car = models.ForeignKey(Car, related_name = 'order', on_delete=models.CASCADE, blank=True, null = True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Order of {self.user.username}"