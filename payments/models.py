from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField('Item', related_name='orders', verbose_name='Товары')
    total_price = models.IntegerField(default=0, verbose_name='Общая стоимость')

    def __str__(self):
        return f"Order {self.pk}"
