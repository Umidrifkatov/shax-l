from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Service

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'is_active', 'order')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title_ru',)}
