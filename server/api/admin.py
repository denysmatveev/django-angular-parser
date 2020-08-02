from django.contrib import admin
from .models import DataList


@admin.register(DataList)
class DataListAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_2019', 'date_2018',
                    'date_2017', 'date_2016')
