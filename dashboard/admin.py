from django.contrib import admin
from .models import *

admin.site.site_header='Erick_inventory_management'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter = ('category',)


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Profile)
