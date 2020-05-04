from django.contrib import admin
from .models import Message
from django.contrib.auth.models import Group

# Register your models here.
class Messages(admin.ModelAdmin):
    list_display = (
        'author',
        'date_started',
        'content',
        'response',
    )
    list_filter = (
        'date_started',
        'author',
        )

admin.site.register(Message, Messages)
admin.site.unregister(Group)
admin.site.site_header = "CoDev-20 Administrator"