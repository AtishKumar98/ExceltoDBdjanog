from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(IPL)
class IPLAdmin(ImportExportModelAdmin):
    list_display = ('team1','team2', 'winner')



# Register your models here.