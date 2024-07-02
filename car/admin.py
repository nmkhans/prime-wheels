from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
  prepopulated_fields = {
    'slug': ('name', 'year_model',)
  }
  list_display = ['name', 'slug']

admin.site.register(Car, CarAdmin)