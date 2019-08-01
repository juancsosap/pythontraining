from django.contrib import admin
from .models import Continent, Country, Region, County, Address, Dictionary

# Register your models here.
class DictionaryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Index', {'fields': ['app','ttype','code','lang']}),
        ('Data',  {'fields': ['value']}),
    ]
    list_display = ('app', 'ttype', 'code', 'lang', 'value')
    list_filter = ['app','ttype','code','lang']
    search_fields = ['app','ttype','code','lang']

admin.site.register(Dictionary, DictionaryAdmin)

admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(County)
admin.site.register(Address)