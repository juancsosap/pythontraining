from django.contrib import admin
from .models import Tenant, MultiTenantUser, Log

# Register your models here.
admin.site.register(Tenant)
admin.site.register(MultiTenantUser)
admin.site.register(Log)
