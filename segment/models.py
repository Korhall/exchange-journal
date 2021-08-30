from django.db import models
import journal.models


# Create your models here.
class Sector(models.Model):
    fieldSectorName = models.CharField(max_length=100, blank=False, null=True, verbose_name='Сектор', default='Нет')
    

    
    class Meta:
        verbose_name_plural = 'Секторы'
        verbose_name = 'Сектор'
        ordering = ['-fieldSectorName']
    
    def __str__(self):
        return self.fieldSectorName


class Branch(models.Model):
    fieldBranchName = models.CharField(max_length=100, blank=False, null=True, verbose_name='Отрасль', default='Нет')
    

    
    class Meta:
        verbose_name_plural = 'Отрасли'
        verbose_name = 'Отрасль'
        ordering = ['-fieldBranchName']
    
    def __str__(self):
        return self.fieldBranchName

class EnterpriseSegment(models.Model):    
    fieldSector = models.ForeignKey('Sector', on_delete=models.CASCADE, verbose_name='Сектор')
    fieldBranch = models.ForeignKey('Branch', on_delete=models.CASCADE, verbose_name='Отрасль')    
    fieldCompanyName = models.CharField(max_length=20, blank=True, null=True, verbose_name='Название компании')
    fieldTicker = models.CharField(max_length=20, blank=True, null=True, verbose_name='Торговое имя')
    

    class Meta:
        verbose_name_plural = 'Сементация компаний'
        verbose_name = 'Сегментация компаний'
        ordering = ['-fieldTicker']

