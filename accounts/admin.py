from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Customizing the User Admin panel
class AccountAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'last_login', 'date_joined', 'is_active']
    search_fields = ['email', 'first_name', 'last_name']  # Search by email, not username
    ordering = ['-date_joined']  # Order users by join date
    readonly_fields = ['last_login', 'date_joined']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)
