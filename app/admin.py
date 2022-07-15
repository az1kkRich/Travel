from django.contrib import admin
from .models import MazzaQilingYayrang, News
# Register your models here.

@admin.register(MazzaQilingYayrang)
class MazzaQilingYayrangAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'malumoti')
    prepopulated_fields = {
        'slug': ['name']
    }

@admin.register(News)
class News(admin.ModelAdmin):
    list_display = ('id','name', 'malumoti')
    prepopulated_fields = {
        'slug': ['name']
    }