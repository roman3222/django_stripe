from django.db import models
from django.contrib.auth.models import User
from typing import List

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('RUB', 'RUB'),
    ('EUR', 'EUR'),
)


class Item(models.Model):
    """
    Модель товара
    """
    name = models.CharField(max_length=50, verbose_name='Имя товара')
    description = models.CharField(max_length=100, verbose_name='Описание товара', null=True, blank=True)
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    currency = models.CharField(verbose_name='Валюта', choices=CURRENCY_CHOICES, default='RUB', max_length=10)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Список товаров'

    def __str__(self):
        return self.name


class Discount(models.Model):
    """
    Модель скидки
    """
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Список скидок'

    def __str__(self):
        return f"{self.name} - {self.amount}%"


class Tax(models.Model):
    """
    Модель налога
    """
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Список налогов'

    def __str__(self):
        return f"{self.name} - {self.rate}%"


class Order(models.Model):
    """
    Модель заказа
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, verbose_name='Товары', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Список заказов'

    def currencies(self) -> List[str]:
        """
        Получить  валюту товаров в заказе
        """
        return self.items.values_list('currency', flat=True).distinct()

    def total_price(self) -> float:
        """
        Функция для подсчета общей суммы заказа с учетом скидки и налога
        """
        total = sum(item.price for item in self.items.all())
        discount_amount = 0
        if self.discount:
            discount_amount = (total * self.discount.amount) / 100

        tax_amount = 0
        if self.tax:
            tax_amount = (total * self.tax.rate) / 100

        sum_price = total - discount_amount + tax_amount
        return sum_price

    def __str__(self):
        return f"Order {self.id}"
