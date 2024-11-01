"""
URL configuration for the Little Lemon project.

The `urlpatterns` list routes URLs to views. For more details, see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function-based views:
    1. Import the view:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

Class-based views:
    1. Import the view:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

Including another URLconf:
    1. Import include(): from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

# Initialize the router and register viewsets
router = DefaultRouter()
router.register(r'tables', views.BookingViewset)

# URL patterns for routing requests
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),  # Booking-related URLs
    path('auth/', include('djoser.urls')),  # Authentication URLs
    path('auth/', include('djoser.urls.authtoken')),
]
