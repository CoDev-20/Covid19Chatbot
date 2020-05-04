from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'firstName',
        'lastName',
        'last_login',
        'is_active',
        'is_admin',
        'is_staff',
        'is_superuser',
        'date_joined',
    )
    
    search_fields = (
        'email',
        'username',
        'firstName',
        'lastName',
    )

    readonly_fields = (
        'date_joined',
        'last_login',
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)