from . import models
from django.contrib import admin

# Register your models here.


class ContentAdmin(admin.ModelAdmin):
    readonly_fields = []
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title', 'rating', 'category', 'is_active']
    list_filter = ['category']
    list_editable = ['category']


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.content, ContentAdmin)

