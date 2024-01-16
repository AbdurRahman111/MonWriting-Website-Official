from django.contrib import admin
from .models import BlogModel, contact_table, Newsletter_table

admin.site.register(BlogModel)


class show_contacts(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'Time']
admin.site.register(contact_table, show_contacts)

class show_Newsletter_table(admin.ModelAdmin):
    list_display = ['email', 'Time']
admin.site.register(Newsletter_table, show_Newsletter_table)

