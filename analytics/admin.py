from django.contrib import admin
from .models import Financial, Operation, Asset

admin.site.register(Financial)
admin.site.register(Operation)
admin.site.register(Asset)
