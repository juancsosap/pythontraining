from django.contrib import admin
from .models import Property, Contact, Owner

# Register your models here.
admin.site.register(Property)
admin.site.register(Contact)
admin.site.register(Owner)