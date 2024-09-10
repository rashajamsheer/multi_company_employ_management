from django.db import models
from django.contrib.auth.models import User

# Company model
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    contact_email = models.EmailField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    # Revert to auto_now_add and auto_now after migration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




