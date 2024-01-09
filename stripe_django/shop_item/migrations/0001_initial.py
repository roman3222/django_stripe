# Generated by Django 5.0.1 on 2024-01-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя заказа')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание заказа')),
                ('price', models.PositiveBigIntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': ('Товар',),
                'verbose_name_plural': ('Список товаров',),
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(related_name='orders', to='shop_item.item', verbose_name='Товары')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Список заказов',
            },
        ),
    ]
