from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import HolidayListSerializer, WishListSerializer, BookingSerializer
from .models import Holiday, Wish, Booking
from rest_framework.permissions import AllowAny, IsAuthenticated


class HolidayViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HolidayListSerializer

    def get_queryset(self):
        queryset = Holiday.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OwnHolidayViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = HolidayListSerializer

    def get_queryset(self):
        queryset = Holiday.objects.filter(user=self.request.user)
        return queryset


class WishViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListSerializer

    def get_queryset(self):
        queryset = Wish.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OwnWishViewSet(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListSerializer

    def get_queryset(self):
        queryset = Wish.objects.filter(user=self.request.user)
        return queryset


class BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.filter(wish_id=self.kwargs["pk"])
        return queryset

    def perform_create(self, serializer):
        wish = Wish.objects.get(id=self.kwargs['pk'])
        return serializer.save(user=self.request.user, wish=wish)


class OwnBookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer

    def get_queryset(self):
        queryset = Booking.objects.filter(user=self.request.user, status=True)
        return queryset
