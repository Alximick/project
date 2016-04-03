from django.contrib import admin
from notes.models import Notes, Category


class Notes_Admin(admin.ModelAdmin):
    fields = ['title', 'text', 'author', 'date', 'favorites', 'category']
    list_display = ['title', 'date']
    list_filter = ['title']
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Notes, Notes_Admin)