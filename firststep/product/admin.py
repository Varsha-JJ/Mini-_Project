import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Product,Category,Color,Size,Filter_Price,Payment,OrderPlaced
# Register your models here.
# admin.site.register(Product)
admin.site.register(Category)
# admin.site.register(Filter_Price)
admin.site.register(Size)
admin.site.register(Payment)
admin.site.register(OrderPlaced)



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


class proColor(admin.ModelAdmin):
    list_display = ['name','code']
    actions = [export_productdetail]

admin.site.register(Color, proColor)    

class proPrice(admin.ModelAdmin):
    list_display = ['price']
    actions = [export_productdetail]

admin.site.register(Filter_Price,proPrice)



     