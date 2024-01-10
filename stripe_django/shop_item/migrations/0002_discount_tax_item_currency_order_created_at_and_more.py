# Generated by Django 5.0.1 on 2024-01-10 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Список скидок',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Список налогов',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('EUR', 'EUR')], default='RUB', max_length=10, verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_item.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop_item.tax'),
        ),
    ]
