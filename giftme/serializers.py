from rest_framework import serializers
from giftme.models import User
from .models import Holiday, Wish, Booking


class HolidayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['id', 'name', 'day', 'month', 'user']
        read_only_fields = ['user']


class BookingSerializer(serializers.ModelSerializer):
    wish = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'status', 'wish', 'date']
        read_only_fields = ['user', 'date']

    def create(self, validated_data):
        status, _ = Booking.objects.update_or_create(
            user=validated_data.get('user', None),
            wish=validated_data.get('wish', None),
            defaults={'status': validated_data.get('status')}
        )
        return status


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
        read_only_fields = ['email']


class WishListSerializer(serializers.ModelSerializer):
    holiday = HolidayListSerializer(many=False, read_only=True)

    class Meta:
        model = Wish
        fields = ['id', 'name', 'description', 'image', 'link', 'holiday', 'user']
        read_only_fields = ['user']

