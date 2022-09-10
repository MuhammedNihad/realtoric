from django.contrib import admin

from .models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "sale_status", "user", "created", "modified")
    list_filter = ("type", "sale_status", "created", "modified")
    search_fields = ("name", "type", "sale_status", "created", "modified")
    date_hierarchy = "created"
    ordering = ("-created",)

    class Meta:
        model = Property
        verbose_name = "Property"
        verbose_name_plural = "Properties"
