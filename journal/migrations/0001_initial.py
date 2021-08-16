# Generated by Django 3.2.6 on 2021-08-11 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldDate', models.DateField(auto_now_add=True, db_index=True, verbose_name='Дата')),
                ('fieldTime', models.TimeField(verbose_name='Время')),
                ('fieldOrderType', models.CharField(max_length=4, verbose_name='Ордер')),
                ('fieldOpenPrice', models.FloatField(max_length=10, null=True, verbose_name='Цена открытия')),
                ('fieldClosePrice', models.FloatField(max_length=10, null=True, verbose_name='Цена закрытия')),
                ('fieldProfit', models.FloatField(max_length=10, null=True, verbose_name='Прибыль')),
                ('fieldTicker', models.CharField(blank=True, max_length=10, null=True, verbose_name='Тикер')),
                ('fieldAmmount', models.IntegerField(blank=True, max_length=7, null=True, verbose_name='Кол-во')),
                ('fieldStopLoss', models.FloatField(blank=True, max_length=10, null=True, verbose_name='Стоп')),
                ('fieldTakeProfit', models.FloatField(blank=True, max_length=10, null=True, verbose_name='Профит')),
                ('fieldLot', models.IntegerField(blank=True, max_length=7, null=True, verbose_name='Лотов')),
                ('fieldEnterReason', models.CharField(blank=True, max_length=20, null=True, verbose_name='Причина входа')),
                ('fieldCloseReason', models.CharField(blank=True, max_length=20, null=True, verbose_name='Причина выхода')),
                ('fieldStrategy', models.CharField(blank=True, max_length=20, null=True, verbose_name='Выбранная стратегия')),
            ],
            options={
                'verbose_name': 'Сделки',
                'verbose_name_plural': 'Сделка',
                'ordering': ['-fieldDate'],
            },
        ),
    ]
