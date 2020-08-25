from django.contrib import admin
from .models import Balance, CreditCard, PastPayments


class CreditCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_name', 'card_number',
                    'expiration_date_month', 'expiration_date_year')
    list_display_links = ('card_name', 'card_number',
                          'expiration_date_month', 'expiration_date_year')
    list_filter = ('user',)
    list_editable = ('user',)
    search_fields = ('card_name', 'user')
    list_per_page = 10


class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amaount')
    list_display_links = ('user',)
    list_filter = ('user',)
    list_editable = ('amaount',)
    search_fields = ('user', 'amaount')
    list_per_page = 10


class PastPaymentsAdmin(admin.ModelAdmin):
    list_display = ('card', 'amaount', 'date')
    list_display_links = ('card', 'date')
    list_filter = ('date',)
    list_editable = ('amaount',)
    search_fields = ('user', 'amaount')
    list_per_page = 10

# Register your models here.


admin.site.register(Balance, BalanceAdmin)
admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(PastPayments, PastPaymentsAdmin)
