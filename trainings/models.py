from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Gym(models.Model):

    name = models.CharField(verbose_name="Название", max_length=255, null=False, blank=False, unique=True)
    address = models.CharField(verbose_name="Адрес", max_length=255, null=True, blank=True, unique=True)


class Currency(models.Model):

    name = models.CharField(verbose_name="Название", max_length=40, null=False, blank=False, unique=True)
    code = models.CharField(verbose_name="Код", max_length=3, null=False, blank=False, unique=True)


class Discount(models.Model):

    percents = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, verbose_name="Скидка", on_delete=models.CASCADE, related_name='discounts')


class Training(models.Model):

    trainer = models.ForeignKey(User, verbose_name="Тренер", on_delete=models.CASCADE, related_name='trainings')
    gym = models.ForeignKey(Gym, verbose_name="Зал", null=True, blank=True, on_delete=models.CASCADE)
    start_time = models.TimeField(verbose_name="Начало", null=True, blank=True)
    end_time = models.TimeField(verbose_name="Конец", null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name="Стоимость", null=True, blank=True)
    discount = models.ForeignKey(Discount, verbose_name="Скидка", null=True, blank=True, on_delete=models.CASCADE)
