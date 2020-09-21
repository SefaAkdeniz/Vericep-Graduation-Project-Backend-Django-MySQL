from django.contrib import admin
from .models import Analysis

# Register your models here.

class AnalysisCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_display_links = ('user', 'date',)
    list_filter = ('user','date')
    list_per_page = 10

admin.site.register(Analysis,AnalysisCardAdmin)