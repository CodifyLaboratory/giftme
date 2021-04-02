from django.urls import path
from .views import HolidayViewSet, WishViewSet

urlpatterns = [
    path('holidays/', HolidayViewSet.as_view({'get': 'list'})),
    path('holidays/<int:pk>', HolidayViewSet.as_view({'get': 'retrieve'})),
    path('holidays/edit/<int:pk>', HolidayViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('holidays/delete/<int:pk>', HolidayViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('holidays/create', HolidayViewSet.as_view({'post': 'create'})),

    path('wishes/', WishViewSet.as_view({'get': 'list'})),
    path('wishes/<int:pk>', WishViewSet.as_view({'get': 'retrieve'})),
    path('wishes/edit/<int:pk>', WishViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('wishes/delete/<int:pk>', WishViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('wishes/create', WishViewSet.as_view({'post': 'create'})),

    path('own-wishes/', WishViewSet.as_view({'get': 'list'})),
    path('own-holidays/', HolidayViewSet.as_view({'get': 'list'})),
]