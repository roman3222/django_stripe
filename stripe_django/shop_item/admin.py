from django.contrib import admin
from .models import Item, Tax, Discount, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """
    Панель управления товарами
    """
    fieldsets = (
        (None, {'fields': ('name', 'description', 'price', 'currency')}),
    )
    list_display = ('id', 'name', 'description', 'price', 'currency')
    search_fields = ('name',)
    list_filter = ('currency', 'price')


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    """
    Панель управления скидками
    """
    fieldsets = (
        (None, {'fields': ('name', 'amount')}),
    )
    list_display = ('id', 'name', 'amount')
    search_fields = ('name',)
    list_filter = ('amount',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    """
    Панель для управления налогами
    """
    fieldsets = (
        (None, {'fields': ('name', 'rate')}),
    )
    list_display = ('id', 'name', 'rate')
    list_filter = ('rate',)


class ItemInline(admin.TabularInline):
    model = Order.items.through
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Панель управления заказами
    """
    fieldsets = (
        (None, {'fields': ('discount', 'tax')}),
    )
    list_display = ('id', 'get_items', 'discount', 'tax', 'created_at', 'total_price')
    list_filter = ('created_at',)
    inlines = [ItemInline]

    def total_price(self, obj):
        """
        Метод для отображения общей суммы(с учетом скидки и налога) заказа впанели управления заказом
        """
        return obj.total_price()

    total_price.short_description = 'Total Price'

    def get_items(self, obj):
        """
        Метод для отображения имени товара в панели управления заказами
        """
        return ', '.join([item.name for item in obj.items.all()])

    get_items.short_description = 'Items'
