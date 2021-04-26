from django.db import models
from user.models import User
from django.contrib.auth import settings


class Holiday(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    day = models.PositiveIntegerField(default=1, verbose_name='Число')
    month = models.CharField(default='Январь', max_length=250, verbose_name='Месяц')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holidays', verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Праздник'
        verbose_name_plural = 'Праздники'


class Wish(models.Model):
    name = models.CharField(max_length=155, verbose_name='Желание')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='wish_pic/', null=True, blank=True, verbose_name='Фотография')
    holiday = models.ForeignKey(Holiday, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Праздник')
    link = models.CharField(max_length=255, null=True, blank=True, verbose_name='Ссылка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishes', verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.BooleanField(verbose_name='Статус')
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE, verbose_name='Желание', related_name='bookings')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'

    def __str__(self):
        return '{}'.format(self.user)
