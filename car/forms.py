from django import forms
from .models import Car

class CarForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'
    exclude = ['slug']

    widgets = {
      'year_model': forms.NumberInput(attrs = {
        'type': 'date'
      })
    }