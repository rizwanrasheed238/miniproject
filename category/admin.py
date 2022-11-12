# from atexit import register
# from itertools import product
from itertools import product
from unicodedata import name
from django.contrib import admin
from .models import Catagory,Product,Subcategory

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Catagory,CategoryAdmin)

class SubategoryAdmin(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Subcategory,SubategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','stock']
admin.site.register(Product,ProductAdmin)






# Register your models here.
