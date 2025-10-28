"""
Certificate in Python Web Framework Development Assistant
Assignment
Student: 16_HoSiuHang_webpage
=========================================================
Steps:
#01 (DONE)Create a new app called analytics under ERB7 by
    python manage.py startapp analytics.

#02 In ERB7/analytics/models.py, define three databases below:
    class Financial(models.Model)
    class Operation(models.Model)
    class Asset(models.Model)

#03 Register the app analytics in ERB7/config/settings.py as:
    INSTALLED_APPS = [
    ...
    'analytics.apps.AnalyticsConfig',
    ...
    ]

#04 Create and apply migrations by
    python manage.py makemigrations analytics
    python manage.py migrate

#05 Enable admin interface and add admin actions.
    In ERB7/analytics/admin.py, execute the following code (This makes
    all three databases manageable via Django Admin):
    from django.contrib import admin
    from .models import Financial, Operation, Asset

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