"""
Certificate in Python Web Framework Development Assistant
Assignment
Student: 16_HoSiuHang_webpage
=======================================================================
Steps:
#01 (DONE)Create a new project called assignment by cloning from ERB7.

#02 (DONE)Create a new app called analytics in assignment by 
        python manage.py startapp analytics.

#03 (DONE)Create a new database called assignment in Postgres by copying clinic.

#04 (DONE)Create local & remote respositories of GitHub & establish the link.
        The remote repository is called assignment.  

#05 (DONE)In assignment/analytics/models.py, define three databases below:
    class Financial(models.Model):
        year_month = models.CharField()
        revenue = models.IntegerField()
        expenses = models.IntegerField()
        profit_loss = models.IntegerField()

    class Operation(models.Model):
        year_month_date = models.CharField()
        manager_name = models.CharField()
        phone_number = models.CharField()

    class Asset(models.Model):
        description = models.CharField()
        purchase_year_month = models.CharField()
        cost = models.IntegerField()
        accu_depre = models.IntegerField()
        net_book_value = models.IntegerField()

    Remarks:
    (a) The Financial class is to record monthly profit and loss data of a company.
    (b) The Operation class is to record names & phone nos of responsible
        managers of a company.
    (c) The Asset class is a fixed assets register for a company.

#06 (DONE)Register the app analytics in assignment/config/settings.py as:
    INSTALLED_APPS = [
    ...
    'analytics.apps.AnalyticsConfig',
    ...
    ]

#07 (DONE)Create and apply migrations by
    python manage.py makemigrations
    python manage.py migrate

#08 (DONE)Enable admin interface. In assignment/analytics/admin.py, execute the 
    following code (This makes all three databases manageable via Django Admin):
    
    from django.contrib import admin
    from .models import Financial, Operation, Asset

    class FinancialAdmin(admin.ModelAdmin):
        list_display = ('year_month', 'revenue_thousand', 'expenditure_thousand', 'profit_loss_thousand')
        list_per_page = 25

    class OperationAdmin(admin.ModelAdmin):
        list_display = ('year_month_day', 'manager_name', 'phone_number')
        list_per_page = 25

    class AssetAdmin(admin.ModelAdmin):
        list_display = ('description', 'purchase_year_month', 'cost_million', 'accu_depre_million', 'net_book_value_million')
        list_per_page = 25

    admin.site.register(Financial, FinancialAdmin)
    admin.site.register(Operation, OperationAdmin)
    admin.site.register(Asset, AssetAdmin)

#09 (DONE)Add "export data" function to built-in admin interface by including the code
    below to assignment/analytics/admin.py:

    import csv
    from django.http import HttpResponse
    def export_as_csv(modeladmin, request, queryset):
        meta = modeladmin.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = "Export Selected to CSV"
    actions = [export_as_csv]

#10 (DONE)Add "import data" function to built-in admin interface by:
    (a) Creating a Simple CSV Upload Form
    (b) Adding Import Logic to Admin Classes
    (c) Extending Admin Classes with Import View
    (d) Creating the Upload Form Template
    (e) Adding Import Button to Admin Interface



"""