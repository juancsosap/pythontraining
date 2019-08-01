from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Provider)
admin.site.register(models.ProviderContact)
admin.site.register(models.CondoProvider)