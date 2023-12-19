from django.contrib import admin
from .models import Category
from .models import Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'created_date', 'updated_date', 'category', 'active']
    readonly_fields = ['image']


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
