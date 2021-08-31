from django.db import models
import segment.models
import datetime 
# Create your models here.


class Notebook(models.Model):
    fieldDate = models.DateField(auto_now=False, auto_now_add=False, db_index=True, blank=False, verbose_name='Дата открытия позиции')
    fieldCloseDate = models.DateField(auto_now=False, auto_now_add=False, blank=False, verbose_name='Дата закрытия позиции', default=datetime.date.today)
    fieldTime = models.TimeField(auto_now=False, auto_now_add=False, blank=False, verbose_name='Время открытия позиции')    
    fieldCloseTime = models.TimeField(auto_now=False, auto_now_add=False, blank=False, verbose_name='Время закрытия позиции')    
    fieldOrderType = models.ForeignKey('OrderType', on_delete=models.PROTECT, verbose_name='Ордер')    
    fieldOpenPrice = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Цена открытия')
    fieldClosePrice = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Цена закрытия')
    fieldProfit = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Прибыль')
    fieldComission = models.FloatField(null=True, blank=False, max_length=10, verbose_name='Прибыль')
    fieldTicker = models.ForeignKey('Ticker', on_delete=models.PROTECT, verbose_name='Тикер') 
    fieldAmmount = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Кол-во')
    fieldStopLoss = models.FloatField(null=True, blank=True, max_length=10, verbose_name='Стоп')
    fieldTakeProfit = models.FloatField(null=True, blank=True, max_length=10, verbose_name='Профит')
    fieldLot = models.IntegerField(max_length=7, blank=True, null=True, verbose_name='Лотов')
    fieldEnterReason = models.ForeignKey('EnterReason', on_delete=models.PROTECT, verbose_name='Причина входа')
    fieldCloseReason = models.ForeignKey('CloseReason', on_delete=models.PROTECT, verbose_name='Причина выхода',default=1, null=True)
    fieldStrategy = models.CharField(max_length=20, blank=True, null=True, verbose_name='Выбранная стратегия')
    fieldMonthTrends = models.ForeignKey('TrendType', on_delete=models.PROTECT, verbose_name='Месячный тренд', default=1, help_text='<p>Если указывать тренд не имеет смысла,<br/> выбирайте значение "Не определено"</p>', related_name='month_trend')
    fieldWeekTrends = models.ForeignKey('TrendType', on_delete=models.PROTECT, verbose_name='Недельный тренд', default=1, related_name='week_trend')
    fieldDayTrends = models.ForeignKey('TrendType', on_delete=models.PROTECT, verbose_name='Дневной тренд', default=1, related_name='day_trend')
    field4HourTrends = models.ForeignKey('TrendType', on_delete=models.PROTECT, verbose_name='4 часовой тренд', default=1, related_name='fourhour_trend')
    field1HourTrends = models.ForeignKey('TrendType', on_delete=models.PROTECT, verbose_name='1 часовой тренд', default=1, related_name='onehour_trend')    
    fieldBranch = models.ForeignKey(segment.models.Branch, on_delete=models.PROTECT, verbose_name='Отрасль',default=1, null=True)
    fieldSector = models.ForeignKey(segment.models.Sector, on_delete=models.PROTECT, verbose_name='Сектор', default=1)
    
    id = models.AutoField(primary_key=True)
    
    
    
    class Meta:
        verbose_name_plural = 'Сделка'
        verbose_name = 'Сделки'
        ordering = ['-fieldDate']


class CloseReason(models.Model):
    
    fieldCloseReason = models.CharField(null=False, blank=False, max_length=25, verbose_name='Причина выхода')
    
    class Meta:
        verbose_name_plural = 'Причины выхода'
        verbose_name = 'Причина выхода'
        ordering = ['-id']
    
    def __str__(self):
        return self.fieldCloseReason


class OrderType(models.Model):
    fieldOrderType = models.CharField(null=False, blank=False, max_length=4, verbose_name='Ордер')
    
    class Meta:
        verbose_name_plural = 'Ордеры'
        verbose_name = 'Ордер'
        ordering = ['-fieldOrderType']
    
    def __str__(self):
        return self.fieldOrderType

class TrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='Тренд')
    
    class Meta:
        verbose_name_plural = 'Тренды'
        verbose_name = 'Тренд'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType
        

class MonthTrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='Месячный тренд')
    
    class Meta:
        verbose_name_plural = 'Месячные тренды'
        verbose_name = 'Месячный Тренд'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType
        
class WeekTrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='Недельный тренд')
    
    class Meta:
        verbose_name_plural = 'Недельные тренды'
        verbose_name = 'Недельный Тренд'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType


class DayTrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='Дневной тренд')
    
    class Meta:
        verbose_name_plural = 'Дневные тренды'
        verbose_name = 'Дневной тренд'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType

class FourHourTrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='4-х часовой тренд')
    
    class Meta:
        verbose_name_plural = '4-х часовые тренды'
        verbose_name = '4-х часовые тренды'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType


class OneHourTrendType(models.Model):
    fieldTrendType = models.CharField(null=False, blank=False, max_length=12, verbose_name='Часовой тренд')
    
    class Meta:
        verbose_name_plural = 'Часовые тренды'
        verbose_name = 'Часовой тренд'
        ordering = ['-fieldTrendType']
    
    def __str__(self):
        return self.fieldTrendType

class Ticker(models.Model):
    fieldTicker = models.CharField(max_length=10, blank=False, null=False, verbose_name='Тикер', default='Нет')
    fieldFullName = models.CharField(max_length=30, blank=False, null=False, verbose_name='Название компании', default='Нет'
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