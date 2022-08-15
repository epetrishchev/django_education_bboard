from django.contrib import admin
from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'rubric', 'published']
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']


class RubricAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)
