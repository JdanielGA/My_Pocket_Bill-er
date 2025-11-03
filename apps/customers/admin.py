# apps/customers/admin.py
from django.contrib import admin
from .models import Customer

# Register the Customer model to make it manageable via the Django admin interface.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'country', 'city', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('last_name', 'first_name')
