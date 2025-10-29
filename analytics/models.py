from django.db import models

class Financial(models.Model):
    year_month = models.CharField()
    revenue_thousand = models.IntegerField()
    expenditure_thousand = models.IntegerField()
    profit_loss_thousand = models.IntegerField()

class Operation(models.Model):
    year_month_day = models.CharField()
    manager_name = models.CharField()
    phone_number = models.CharField()

class Asset(models.Model):
    description = models.CharField()
    purchase_year_month = models.CharField()
    cost_million = models.IntegerField()
    accu_depre_million = models.IntegerField()
    net_book_value_million = models.IntegerField()
