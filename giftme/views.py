from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import HolidayListSerializer, WishListSerializer
from .models import Holiday, Wish
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