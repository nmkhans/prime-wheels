from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.UserRegisterView.as_view(), name = 'user-register'),
  path('login/', views.UserLoginView.as_view(), name = 'user-login'),
  path('logout/', views.user_logout, name = 'user-logout'),
  path('profile/', views.UserProfileView.as_view(), name = 'user-profile'),
  path('update/<int:id>/', views.UserUpdateView.as_view(), name = 'user-update'),
  path('password-update/', views.UserPasswordUpdateView.as_view(), name = 'user-password-update'),
  path('all-orders', views.all_orders, name = 'all-orders')
]