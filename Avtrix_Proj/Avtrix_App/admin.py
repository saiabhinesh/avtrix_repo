from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Order

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Order,OrderAdmin)  
