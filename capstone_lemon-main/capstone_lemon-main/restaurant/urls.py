from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import MenuItemView, MenuDetailView

urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu'),  # Menu list and creation endpoint
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu-item'),  # Specific menu item endpoint
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Djoser authentication endpoints
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
