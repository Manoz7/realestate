from django.contrib import admin

# Register your models here.

from .models import Listing, PropertyType


class ListingAdmin(admin.ModelAdmin):
    # list_display = ('property_id', 'title', 'is_published',
    #                 'price', 'list_data', 'realtor')
    list_display = ('property_id', 'title', 'is_published',
                    'price', 'list_data')
    list_display_links = ('property_id', 'title')
    # list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)

admin.site.register(PropertyType)