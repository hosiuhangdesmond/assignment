import csv
from django.http import HttpResponse
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render, redirect
from .models import Financial, Operation, Asset
from .forms import SimpleCSVImportForm

def simple_csv_import(modeladmin, request, model):
    if request.method == "POST":
        form = SimpleCSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            try:
                for row in reader:
                    model.objects.create(**row)
                messages.success(request, "CSV imported successfully.")
            except Exception as e:
                messages.error(request, f"Import failed: {str(e)}")
            return redirect(request.path)
    else:
        form = SimpleCSVImportForm()

    context = {
        'form': form,
        'title': 'Import CSV',
        'opts': model._meta,
    }
    return render(request, "admin/csv_form.html", context)

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

class FinancialAdmin(admin.ModelAdmin):
    list_display = ('year_month', 'revenue_thousand', 'expenditure_thousand', 'profit_loss_thousand')
    list_per_page = 25
    actions = [export_as_csv]

    change_list_template = "admin/analytics/financial/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv), name='financial_import_csv'),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return simple_csv_import(self, request, Financial)

class OperationAdmin(admin.ModelAdmin):
    list_display = ('year_month_day', 'manager_name', 'phone_number')
    list_per_page = 25
    actions = [export_as_csv]

    change_list_template = "admin/analytics/operation/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv), name='operation_import_csv'),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return simple_csv_import(self, request, Operation)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('description', 'purchase_year_month', 'cost_million', 'accu_depre_million', 'net_book_value_million')
    list_per_page = 25
    actions = [export_as_csv]

    change_list_template = "admin/analytics/asset/change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.admin_site.admin_view(self.import_csv), name='asset_import_csv'),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        return simple_csv_import(self, request, Asset)

admin.site.register(Financial, FinancialAdmin)
admin.site.register(Operation, OperationAdmin)
admin.site.register(Asset, AssetAdmin)
