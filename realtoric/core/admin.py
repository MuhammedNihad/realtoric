from django.contrib import admin

from .models import (
    Apartment,
    ApartmentImage,
    Commercial,
    CommercialImage,
    House,
    HouseImage,
    Land,
    LandImage,
    Villa,
    VillaImage,
)


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_title", "user", "listed_on", "modified_on")
    list_filter = (
        "sell_or_rent",
        "sale_status",
        "rent_status",
        "listed_on",
        "modified_on",
    )
    search_fields = ("ad_title", "user", "city", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = Apartment
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"


@admin.register(ApartmentImage)
class ApartmentImageAdmin(admin.ModelAdmin):
    list_display = ("id", "apartment", "image", "listed_on", "modified_on")
    list_filter = ("listed_on", "modified_on")
    search_fields = ("apartment", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = ApartmentImage
        verbose_name = "Apartment Image"
        verbose_name_plural = "Apartment Images"


@admin.register(Commercial)
class CommercialAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_title", "user", "listed_on", "modified_on")
    list_filter = (
        "sell_or_rent",
        "sale_status",
        "rent_status",
        "listed_on",
        "modified_on",
    )
    search_fields = ("ad_title", "user", "city", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = Commercial
        verbose_name = "Commercial"
        verbose_name_plural = "Commercials"


@admin.register(CommercialImage)
class CommercialImageAdmin(admin.ModelAdmin):
    list_display = ("id", "commercial", "image", "listed_on", "modified_on")
    list_filter = ("listed_on", "modified_on")
    search_fields = ("commercial", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = CommercialImage
        verbose_name = "Commercial Image"
        verbose_name_plural = "Commercial Images"


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_title", "user", "listed_on", "modified_on")
    list_filter = (
        "sell_or_rent",
        "sale_status",
        "rent_status",
        "listed_on",
        "modified_on",
    )
    search_fields = ("ad_title", "user", "city", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = House
        verbose_name = "House"
        verbose_name_plural = "Houses"


@admin.register(HouseImage)
class HouseImageAdmin(admin.ModelAdmin):
    list_display = ("id", "house", "image", "listed_on", "modified_on")
    list_filter = ("listed_on", "modified_on")
    search_fields = ("house", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = HouseImage
        verbose_name = "House Image"
        verbose_name_plural = "House Images"


@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_title", "user", "listed_on", "modified_on")
    list_filter = (
        "sell_or_rent",
        "sale_status",
        "rent_status",
        "listed_on",
        "modified_on",
    )
    search_fields = ("ad_title", "user", "city", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = Land
        verbose_name = "Land"
        verbose_name_plural = "Lands"


@admin.register(LandImage)
class LandImageAdmin(admin.ModelAdmin):
    list_display = ("id", "land", "image", "listed_on", "modified_on")
    list_filter = ("listed_on", "modified_on")
    search_fields = ("land", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = LandImage
        verbose_name = "Land Image"
        verbose_name_plural = "Land Images"


@admin.register(Villa)
class VillaAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_title", "user", "listed_on", "modified_on")
    list_filter = (
        "sell_or_rent",
        "sale_status",
        "rent_status",
        "listed_on",
        "modified_on",
    )
    search_fields = ("ad_title", "user", "city", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = Villa
        verbose_name = "Villa"
        verbose_name_plural = "Villas"


@admin.register(VillaImage)
class VillaImageAdmin(admin.ModelAdmin):
    list_display = ("id", "villa", "image", "listed_on", "modified_on")
    list_filter = ("listed_on", "modified_on")
    search_fields = ("villa", "listed_on", "modified_on")
    date_hierarchy = "listed_on"
    ordering = ("-listed_on",)

    class Meta:
        model = VillaImage
        verbose_name = "Villa Image"
        verbose_name_plural = "Villa Images"


# Customize the admin site title and header
admin.site.site_header = "Realtoric Admin Panel"
admin.site.site_title = "Realtoric Admin Panel"
admin.site.index_title = "Welcome to Realtoric Panel"
