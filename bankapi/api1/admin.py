from django.contrib import admin
from api1.models import Bank, Customer
# Register your models here.


class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'bank')
    list_filter = ('bank', )


admin.site.register(Bank, BankAdmin)
admin.site.register(Customer, CustomerAdmin)
