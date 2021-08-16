from django.db import models

# Create your models here.
from django.db import models

class Notebook(models.Model):
    fieldDate = models.DateField(auto_now=False, auto_now_add=True, db_index=True, blank=False, verbose_name='Дата')
    fieldTime = models.TimeField(auto_now=False, auto_now_add=False, blank=False, verbose_name='Время')    
    fieldOrderType = models.ForeignKey('OrderType', on_delete=models.CASCADE, verbose_name='Ордер')    
    fieldOpenPrice = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Цена открытия')
    fieldClosePrice = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Цена закрытия')
    fieldProfit = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Прибыль')
    fieldTicker = models.ForeignKey('Ticker', on_delete=models.CASCADE, verbose_name='Тикер') 
    fieldAmmount = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Кол-во')
    fieldStopLoss = models.FloatField(null=True, blank=True, max_length=10, verbose_name='Стоп')
    fieldTakeProfit = models.FloatField(null=True, blank=True, max_length=10, verbose_name='Профит')
    fieldLot = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Лотов')
    fieldEnterReason = models.ForeignKey('EnterReason', on_delete=models.CASCADE, verbose_name='Причина входа')
    fieldCloseReason = models.CharField(max_length=20, blank=True, null=True, verbose_name='Причина выхода')
    fieldStrategy = models.CharField(max_length=20, blank=True, null=True, verbose_name='Выбранная стратегия')
    
    
    class Meta:
        verbose_name_plural = 'Сделка'
        verbose_name = 'Сделки'
        ordering = ['-fieldDate']


class OrderType(models.Model):
    fieldOrderType = models.CharField(null=False, blank=False, max_length=4, verbose_name='Ордер')
    
    class Meta:
        verbose_name_plural = 'Ордеры'
        verbose_name = 'Ордер'
        ordering = ['-fieldOrderType']
    
    def __str__(self):
        return self.fieldOrderType


class Ticker(models.Model):
    fieldTicker = models.CharField(max_length=10, blank=False, null=False, verbose_name='Тикер', default='Нет')
    fieldFullName = models.CharField(max_length=20, blank=False, null=False, verbose_name='Название компании', default='Нет'
)
    
    class Meta:
        verbose_name_plural = 'Тикеры'
        verbose_name = 'Тикер'
        ordering = ['-fieldTicker']
    
    def __str__(self):
        return self.fieldTicker

class EnterReason(models.Model):
    fieldEnterReason = models.CharField(null=False, blank=False, max_length=10, verbose_name='Причина входа', default='Нет')
    
    class Meta:
        verbose_name_plural = 'Причины входа'
        verbose_name = 'Причина входа'
        ordering = ['-fieldEnterReason']
    
    def __str__(self):
        return self.fieldEnterReason