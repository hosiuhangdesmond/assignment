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

    admin.site.register(Financial)
    admin.site.register(Operation)
    admin.site.register(Asset)


#05  and add admin actions.
    

    class FinancialAdmin(admin.ModelAdmin):
        actions = ['clear_records', 'format_records', 'export_records', 
    'import_records']
    def clear_records(self, request, queryset):
    ...
    def format_records(self, request, queryset):
    ...
    def export_records(self, request, queryset):
    ...
    def import_records(self, request, queryset):
    ...

    class OperationAdmin(admin.ModelAdmin):
        actions = ['clear_records', 'format_records', 'export_records', 
    'import_records']
    def clear_records(self, request, queryset):
    ...
    def format_records(self, request, queryset):
    ...
    def export_records(self, request, queryset):
    ...
    def import_records(self, request, queryset):
    ...

    class AssetAdmin(admin.ModelAdmin):
        actions = ['clear_records', 'format_records', 'export_records', 
    'import_records']
    def clear_records(self, request, queryset):
    ...
    def format_records(self, request, queryset):
    ...
    def export_records(self, request, queryset):
    ...
    def import_records(self, request, queryset):
    ...

    admin.site.register(Financial, FinancialAdmin)
    admin.site.register(Operation, OperationAdmin)
    admin.site.register(Asset, AssetAdmin)

#06 Handle external disk operations.

"""