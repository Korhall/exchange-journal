from django.contrib import admin
from .models import Notebook, OrderType, Ticker, EnterReason

# Register your models here.
@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = ('fieldDate', 'fieldTime', 'fieldOrderType', 'fieldOrderType', 'fieldOpenPrice', 'fieldClosePrice', 'fieldProfit', 'fieldTicker', 'fieldAmmount', 'fieldStopLoss', 'fieldTakeProfit', 'fieldLot',  'fieldEnterReason', 'fieldCloseReason', 'fieldStrategy')
    list_display_links = ('fieldDate', 'fieldTime', 'fieldOrderType', 'fieldEnterReason', 'fieldCloseReason')
    


@admin.register(OrderType)
class OrderTypeAdmin(admin.ModelAdmin):
    list_display = ('fieldOrderType',)
    list_display_links = ('fieldOrderType',)


@admin.register(Ticker)
class TickerAdmin(admin.ModelAdmin):
    list_display = ('fieldTicker', 'fieldFullName',)
    list_display_links = ('fieldTicker','fieldFullName',)


@admin.register(EnterReason)
class EnterReasonAdmin(admin.ModelAdmin):
    list_display = ('fieldEnterReason',)
    list_display_links = ('fieldEnterReason',)