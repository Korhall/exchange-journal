from django.contrib import admin
from .models import Notebook, OrderType, Ticker, EnterReason, TrendType, CloseReason, OneHourTrendType, FourHourTrendType, DayTrendType, WeekTrendType, MonthTrendType
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Notebook)
class NotebookAdmin(ImportExportModelAdmin):
    list_display = ('id',  'fieldDate', 'fieldCloseDate', 'fieldTime', 'fieldCloseTime', 'fieldOrderType',  'fieldOpenPrice', 'fieldClosePrice', 'fieldProfit', 'fieldComission', 'fieldTicker', 'fieldAmmount', 'fieldStopLoss', 'fieldTakeProfit', 'fieldLot',  'fieldEnterReason', 'fieldCloseReason', 'fieldStrategy', 'fieldMonthTrends', 'fieldWeekTrends', 'fieldDayTrends', 'field4HourTrends', 'field1HourTrends', 'fieldBranch', 'fieldSector')
    list_display_links = ('id',)
    
    
    list_editable = [ 'fieldDate', 'fieldCloseDate', 'fieldTime', 'fieldCloseTime',  'fieldOrderType', 'fieldOpenPrice', 'fieldClosePrice', 'fieldProfit', 'fieldComission', 'fieldTicker', 'fieldAmmount', 'fieldStopLoss', 'fieldTakeProfit', 'fieldLot',  'fieldEnterReason', 'fieldCloseReason', 'fieldStrategy', 'fieldBranch', 'fieldSector', 'fieldMonthTrends', 'fieldWeekTrends', 'fieldDayTrends', 'field4HourTrends', 'field1HourTrends',]
    list_filter = (
        'fieldOrderType', 'fieldEnterReason', 'fieldCloseReason', 'fieldStrategy',  'fieldMonthTrends', 'fieldWeekTrends', 'fieldDayTrends', 'field4HourTrends', 'field1HourTrends', 'fieldBranch', 'fieldSector'
    )
    search_fields = ('fieldTicker',)    
    
@admin.register(TrendType)
class TrendTypeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'fieldTrendType',)
    list_display_links = ('id',)
    
    
    list_editable = ['fieldTrendType',]
    
    
@admin.register(CloseReason)
class CloseReasonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'fieldCloseReason',)
    list_display_links = ('id',)
    
    
    list_editable = ['fieldCloseReason',]

    
class NotebookResource(resources.ModelResource):
    
    class Meta:
        model = Notebook
        fields = ('fieldDate', 'fieldTime', 'fieldOrderType', 'fieldOrderType', 'fieldOpenPrice', 'fieldClosePrice', 'fieldProfit', 'fieldTicker', 'fieldAmmount', 'fieldStopLoss', 'fieldTakeProfit', 'fieldLot',  'fieldEnterReason', 'fieldCloseReason', 'fieldStrategy', 'fieldMonthTrend', 'fieldWeekTrend', 'fieldDayTrend', 'field4HourTrend', 'field1HourTrend',)
        skip_unchanged = True
        report_skiped = False

@admin.register(OrderType)
class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('fieldOrderType',)
    list_display_links = ('fieldOrderType',)


@admin.register(Ticker)
class TickerAdmin(ImportExportModelAdmin):
    list_display = ('fieldTicker', 'fieldFullName',)
    list_display_links = ('fieldTicker','fieldFullName',)

class TickerResource(resources.ModelResource):
    
    class Meta:
        model = Ticker
        fields = ('fieldTicker', 'fieldFullName',)
        skip_unchanged = True
        report_skiped = False


@admin.register(EnterReason)
class EnterReasonAdmin(admin.ModelAdmin):
    list_display = ('fieldEnterReason',)
    list_display_links = ('fieldEnterReason',)