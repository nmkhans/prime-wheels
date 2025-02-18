from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('filter/<slug:brand_slug>/', views.home, name = 'filter-home'),
    path('users/', include('users.urls')),
    path('cars/', include('car.urls')),
    path('brands/', include('brand.urls')),
    path('comments/', include('comments.urls')),
    path('orders/', include('order.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)