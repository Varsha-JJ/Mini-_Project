import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Product,Category,Color,Size
# Register your models here.
# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)

def export_productdetail(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="productdetail.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name','Category','Price'])
    product = queryset.values_list('name','category','price')
    for i in product:
        writer.writerow(i)
    return response


export_productdetail.short_description = 'Export to csv'


class proAdmin(admin.ModelAdmin):
    list_display = ['name','price','publish']
    actions = [export_productdetail]


admin.site.register(Product, proAdmin)