from django.contrib import admin

from .models import CategoryL1, CategoryL2, Product


class CategoryL1Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class CategoryL2Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    readonly_fields = ["image_small", "image_thumb"]


admin.site.register(CategoryL1, CategoryL1Admin)
admin.site.register(CategoryL2, CategoryL2Admin)
admin.site.register(Product, ProductAdmin)
