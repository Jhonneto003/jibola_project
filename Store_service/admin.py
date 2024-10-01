from django.contrib import admin
from .models import Store, Products ,Category

# Register your models here.

class StoreServiceAdmin(admin.ModelAdmin):
    list_display=[ 'id', 'owner', 'name_of_store']
    list_display_links = [ 'id', 'owner', 'name_of_store']
    list_filter=[]

class CategoryServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','description']
    list_display_links =[ 'id', 'name']
    list_filter = []

class ProductServiceAdmin(admin.ModelAdmin):
    list_display=['id', 'name','owner']
    list_display_links = ['id','name', 'owner']

admin.site.register(Products, ProductServiceAdmin)
admin.site.register(Category,CategoryServiceAdmin)
admin.site.register(Store,StoreServiceAdmin)