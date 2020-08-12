from django.contrib import admin
from .models import MlModel,ModelInput


class MlModelAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'heroku_url', 'created_date', 'isPublished')
    list_display_links = ('model_name', 'heroku_url', 'created_date')
    list_filter = ('created_date', 'isPublished')
    list_editable = ('isPublished',)
    search_fields = ('model_name', 'model_description')
    list_per_page = 10

class ModelInputAdmin(admin.ModelAdmin):
    list_display = ('input_name','typed','model_id')
    list_display_links = ('input_name','model_id')
    list_filter = ('typed','model_id')
    list_editable = ('typed',)
    search_fields = ('input_name','typed','model_id')
    list_per_page = 10
    


# Register your models here.
admin.site.register(MlModel, MlModelAdmin)
admin.site.register(ModelInput,ModelInputAdmin)
