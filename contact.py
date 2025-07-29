INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'contacts',
]
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone')
