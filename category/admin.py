from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    display = ('category_title')


admin.site.register(Category, CategoryAdmin)
