# Generated by Django 3.1.7 on 2021-04-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftme', '0002_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='date',
        ),
        migrations.AddField(
            model_name='holiday',
            name='day',
            field=models.PositiveIntegerField(default=1, verbose_name='Число'),
        ),
        migrations.AddField(
            model_name='holiday',
            name='month',
            field=models.CharField(default='Январь', max_length=250, verbose_name='Месяц'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка'),
        ),
    ]
