from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from datetime import date


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(db_index=True, unique=True, blank=False, verbose_name='Почта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    birth_date = models.DateField(default=date.today, verbose_name='Дата рождения')
    facebook_link = models.CharField(max_length=50, blank=True, null=True, verbose_name='Социальные сети')
    instagram_link = models.CharField(max_length=50, blank=True, null=True, verbose_name='Социальные сети')
    photo = models.ImageField(upload_to='profile-photo/', blank=True, null=True, verbose_name='Фотография')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'