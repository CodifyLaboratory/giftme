from rest_framework import serializers
from .models import Holiday, Wish


class HolidayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holiday
        fields = ['id', 'name', 'date', 'user']


class WishListSerializer(serializers.ModelSerializer):
    holiday = HolidayListSerializer(many=False, read_only=True)

    class Meta:
        model = Wish
        fields = ['id', 'name', 'description', 'image', 'link', 'holiday', 'user']
