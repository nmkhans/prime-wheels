from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm, UserUpdateForm
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.models import User
from order.models import Order
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class UserRegisterView(CreateView):
  template_name = 'users/user_registration.html'
  form_class = UserRegisterForm
  success_url = reverse_lazy('home')

  def form_valid(self, form):
    messages.success(self.request, 'Account created. Login to continue.')
    return super().form_valid(form)
  
class UserLoginView(LoginView):
  template_name = 'users/user_login.html'

  def form_valid(self, form):
    messages.success(self.request, 'Login successfull.')
    return super().form_valid(form)
  
  def get_success_url(self):
    return reverse_lazy('home')
  
@login_required
def user_logout(req):
  logout(req)
  messages.warning(req, 'Logout successfull')
  return redirect('home')

@method_decorator(login_required, name = 'dispatch')
class UserProfileView(TemplateView):
  template_name = 'users/user_profile.html'
  
  def get_context_data(self, **kwargs):
    kwargs['user'] = self.request.user
    return kwargs
  
@method_decorator(login_required, name = 'dispatch')
class UserUpdateView(UpdateView):
  template_name = 'users/user_update.html'
  model = User
  form_class = UserUpdateForm
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('user-profile')

  def form_valid(self, form):
    messages.success(self.request, 'Profile updated.')
    return super().form_valid(form)
  
@method_decorator(login_required, name = 'dispatch')
class UserPasswordUpdateView(PasswordChangeView):
  template_name = 'users/user_password_update.html'
  success_url = reverse_lazy('user-profile')

  def form_valid(self, form):
    messages.success(self.request, 'Password updated.')
    return super().form_valid(form)

@login_required
def all_orders(req):
  user = User.objects.get(username = req.user.username)
  orders = Order.objects.filter(user = user).order_by('-created_at')

  return render(req, 'users/user_all_order.html', {
    'orders': orders
  })