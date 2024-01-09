from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя заказа')
    description = models.CharField(max_length=100, verbose_name='Описание заказа', null=True, blank=True)
    price = models.PositiveBigIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар',
        verbose_name_plural = 'Список товаров',
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Товары', related_name='orders')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Список заказов'

