from django.contrib import admin
from .models import MlModel


class MlModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'heroku_url', 'created_date', 'isPublished')
    list_display_links = ('model_name', 'heroku_url', 'created_date')
    list_filter = ('created_date', 'isPublished')
    list_editable = ('isPublished',)
    search_fields = ('model_name', 'model_description')
    list_per_page = 10
    


# Register your models here.
admin.site.register(MlModel, MlModelAdmin)
