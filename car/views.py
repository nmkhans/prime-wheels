from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Car
from .forms import CarForm
from django.views.generic import CreateView
from django.template.defaultfilters import slugify
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def car_detail(req, slug_name):
  car = Car.objects.get(slug = slug_name)
  return render(req, 'car/car_detail.html', {
    'car': car
  })

@method_decorator(login_required, name = 'dispatch')
class CarAddView(CreateView):
  template_name = 'car/car_add.html'
  form_class = CarForm
  model = Car
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.slug = slugify(f"{self.object.name} {self.object.year_model}")
    self.object.save()

    messages.success(self.request, 'Car added.')
    return super().form_valid(form)