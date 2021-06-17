from django.contrib import admin
from.models import *
from django.utils.text import slugify

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Images

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    inlines = [ImageInline]


admin.site.register(Images)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':(slugify('name'),)}