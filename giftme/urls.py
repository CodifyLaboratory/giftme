from django.urls import path
from .views import HolidayViewSet, WishViewSet, BookingViewSet, OwnBookingViewSet, OwnHolidayViewSet, OwnWishViewSet, \
    ShareWishViewSet

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
    path('wishes/share/<int:pk>', ShareWishViewSet.as_view({'get': 'list'})),

    path('own-wishes/', OwnWishViewSet.as_view({'get': 'list'})),
    path('own-holidays/', OwnHolidayViewSet.as_view({'get': 'list'})),
    path('own-bookings/', OwnBookingViewSet.as_view({'get': 'list'})),

    path('booking/create/<int:pk>', BookingViewSet.as_view({'post': 'create'})),
    path('booking/edit/<int:pk>', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('booking/delete/<int:pk>', BookingViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('booking/<int:pk>', BookingViewSet.as_view({'get': 'retrieve'})),

]
