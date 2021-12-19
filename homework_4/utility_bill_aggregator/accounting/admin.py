from django.contrib import admin
from accounting.models import Service, Account

class ServiceAdmin(admin.ModelAdmin):
    pass

class AccountAdmin(admin.ModelAdmin):
     list_filter = ('is_paid', 'month')
     search_fields = ['personal_account']

admin.site.register(Service, ServiceAdmin)
admin.site.register(Account, AccountAdmin)