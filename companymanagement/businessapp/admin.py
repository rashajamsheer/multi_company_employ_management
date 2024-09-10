from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'created_at')
    search_fields = ('name', 'contact_email')
    list_filter = ('created_at',)




