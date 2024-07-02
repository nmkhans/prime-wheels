from django.db import models
from brand.models import Brand
from django.core.validators import MinLengthValidator

# Create your models here.
class Car(models.Model):
  name = models.CharField(max_length = 100)
  year_model = models.DateField()
  slug = models.SlugField()
  description = models.TextField()
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
  price = models.IntegerField(null=True, blank=True)
  quantity = models.IntegerField(null=True, blank=True)
  image = models.ImageField(upload_to='')
