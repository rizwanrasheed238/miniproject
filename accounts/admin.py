import csv
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from .models import Account
from django.utils.html import format_html
# Register your models here.

#csv file downloader
def export_users(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email','Phone No'])
    Account = queryset.values_list('fname','email', 'phone_number')
    for user in Account:
        writer.writerow(user)
    return response
export_users.short_description = 'Download Customer Details'


class AccountAdmin(UserAdmin):
    exclude =('password',)

    list_display = (
        'email', 'fname', 'lname', 'last_login', 'is_active', 'date_joined'
    )
    list_display_links = (
        'email', 'fname', 'lname',
    )
    readonly_fields = (
        'last_login', 'date_joined',
    )
    ordering = (
        '-date_joined',
    )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions=[export_users]
admin.site.register(Account, AccountAdmin)
#
# class UserAdmin(admin.ModelAdmin):
#     exclude =('password',)

# admin.site.register(Account,UserAdmin)



