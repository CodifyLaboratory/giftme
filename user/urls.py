from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'})),

]