from django.contrib import admin
from .models import Condo, Address, Property
# Register your models here.
admin.site.register(Condo)
admin.site.register(Address)
admin.site.register(Property)