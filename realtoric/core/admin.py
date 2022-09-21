from django.contrib import admin

from .models import Property, PropertyImage


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "sale_status", "user", "created", "modified")
    list_filter = ("type", "sale_status", "created", "modified")
    search_fields = ("name", "type", "sale_status", "created", "modified")
    date_hierarchy = "created"
    ordering = ("-created",)

    class Meta:
        model = Property
        verbose_name = "Property"
        verbose_name_plural = "Properties"


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("id", "property", "image", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("property", "created", "modified")
    date_hierarchy = "created"
    ordering = ("-created",)

    class Meta:
        model = PropertyImage
        verbose_name = "Property Image"
        verbose_name_plural = "Property Images"


# Customize the admin site title and header
admin.site.site_header = "Realtoric Admin Panel"
admin.site.site_title = "Realtoric Admin Panel"
admin.site.index_title = "Welcome to Realtoric Panel"
