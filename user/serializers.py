from rest_framework import serializers
from .models import User
from giftme.serializers import HolidayListSerializer, WishListSerializer


class UserDetailSerializer(serializers.ModelSerializer):
    holidays = HolidayListSerializer(many=True, read_only=True)
    wishes = WishListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'description', 'birth_date', 'facebook_link', 'instagram_link',
            'photo', 'holidays', 'wishes']
        read_only_fields = ['email']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 'description', 'birth_date', 'facebook_link', 'instagram_link',
            'photo']
        read_only_fields = ['email']