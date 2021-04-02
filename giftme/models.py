from django.db import models
from user.models import User


class Holiday(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    date = models.DateField(null=True, blank=True, verbose_name='Дата')
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
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishes', verbose_name='Пользователь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Желание'
        verbose_name_plural = 'Желания'
