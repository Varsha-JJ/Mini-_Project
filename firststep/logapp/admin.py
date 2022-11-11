import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Account

from django.contrib.auth.models import Group
# Register your models here.
# admin.site.register(Account)
admin.site.unregister(Group)

def export_log(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="login.csv"'
    writer = csv.writer(response)
    writer.writerow(['Firstname','Lastname','Address','Email','Contact','City','State','Pincode','Password'])
    login = queryset.values_list('first_name', 'last_name','address','email','contact','city','state','pincode','password')
    for i in login:
        writer.writerow(i)
    return response


export_log.short_description = 'Export to csv'


class LogAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','contact','email']
    actions = [export_log]


admin.site.register(Account, LogAdmin)


