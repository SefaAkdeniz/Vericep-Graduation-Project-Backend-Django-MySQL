from django.contrib import admin
from .models import Balance,CreditCard,PastPayments


# Register your models here.

admin.site.register(Balance)
admin.site.register(CreditCard)
admin.site.register(PastPayments)
