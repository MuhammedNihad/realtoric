from django import forms

from .models import Apartment, City, Commercial, House, Land, Villa


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        to_field_name="name",
        empty_label="Cities",
        label="",
    )


class PropertyBaseFormMixin(forms.ModelForm):
    """
    Form mixin for common fields to prevent code duplication.
    """

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Select City",
    )

    widgets = {
        "ad_title": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mention the key features of the property...",
            }
        ),
        "description": forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter a description. Eg: Include condition, reason for selling, etc...",
            }
        ),
        "address": forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Enter address..."}
        ),
        "google_map": forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "Copy and paste Google maps link...",
            }
        ),
        "contact_info": forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter contact number or email...",
            }
        ),
    }


class ApartmentPostForm(PropertyBaseFormMixin):
    """
    Form to create a new Apartment.
    """

    class Meta:
        model = Apartment
        fields = [
            "bedroom",
            "bathroom",
            "area",
            "floor",
            "ad_title",
            "description",
            "address",
            "city",
            "google_map",
            "contact_info",
        ]
        widgets = PropertyBaseFormMixin.widgets

    field_order = [
        "bedroom",
        "bathroom",
        "area",
        "floor",
        "ad_title",
        "description",
        "images",
        "address",
        "city",
        "google_map",
        "contact_info",
    ]


class CommercialPostForm(PropertyBaseFormMixin):
    """
    Form to create a new Commercial property.
    """

    class Meta:
        model = Commercial
        fields = [
            "commercial_type",
            "area",
            "floor",
            "ad_title",
            "description",
            "address",
            "city",
            "google_map",
            "contact_info",
        ]
        widgets = PropertyBaseFormMixin.widgets

    field_order = [
        "commercial_type",
        "area",
        "floor",
        "ad_title",
        "description",
        "images",
        "address",
        "city",
        "google_map",
        "contact_info",
    ]


class HousePostForm(PropertyBaseFormMixin):
    """
    Form to create a new House.
    """

    class Meta:
        model = House
        fields = [
            "bedroom",
            "bathroom",
            "area",
            "floor",
            "ad_title",
            "description",
            "address",
            "city",
            "google_map",
            "contact_info",
        ]
        widgets = PropertyBaseFormMixin.widgets

    field_order = [
        "bedroom",
        "bathroom",
        "area",
        "floor",
        "ad_title",
        "description",
        "images",
        "address",
        "city",
        "google_map",
        "contact_info",
    ]


class LandPostForm(PropertyBaseFormMixin):
    """
    Form to create a new Land.
    """

    class Meta:
        model = Land
        fields = [
            "land_type",
            "plot_area",
            "length",
            "breadth",
            "road_accessible",
            "ad_title",
            "description",
            "address",
            "city",
            "google_map",
            "contact_info",
        ]
        widgets = PropertyBaseFormMixin.widgets

    field_order = [
        "land_type",
        "plot_area",
        "length",
        "breadth",
        "road_accessible",
        "ad_title",
        "description",
        "images",
        "address",
        "city",
        "google_map",
        "contact_info",
    ]


class VillaPostForm(PropertyBaseFormMixin):
    """
    Form to create a new Villa.
    """

    class Meta:
        model = Villa
        fields = [
            "bedroom",
            "bathroom",
            "area",
            "floor",
            "ad_title",
            "description",
            "address",
            "city",
            "google_map",
            "contact_info",
        ]
        widgets = PropertyBaseFormMixin.widgets

    field_order = [
        "bedroom",
        "bathroom",
        "area",
        "floor",
        "ad_title",
        "description",
        "images",
        "address",
        "city",
        "google_map",
        "contact_info",
    ]
