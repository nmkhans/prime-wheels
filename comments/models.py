from django.db import models
from car.models import Car

# Create your models here.
class Comment(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  car = models.ForeignKey(Car, on_delete=models.Case, blank=True, null=True, related_name="comment")

  def __str__(self):
    return f"{self.name}"