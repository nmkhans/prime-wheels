from django.urls import reverse_lazy
from .forms import BrandForm
from .models import Brand
from django.views.generic import CreateView
from django.template.defaultfilters import slugify
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class BrandAddView(CreateView):
  template_name = 'brand/brand_add.html'
  model = Brand
  form_class = BrandForm
  success_url = reverse_lazy('home')
  
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.slug = slugify(self.object.name)
    self.object.save()
    messages.success(self.request, 'Brand added')
    
    return super().form_valid(form)