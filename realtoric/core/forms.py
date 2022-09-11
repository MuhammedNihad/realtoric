from django import forms

from .models import Property

# from django.utils.translation import gettext_lazy as _


class PostPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "name",
            "description",
            "type",
            "address",
            "city",
            "google_maps",
            "image",
            "contact_info",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Name of property..."}
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter description. eg: 1bhk, 50 cent...",
            }
        )
        self.fields["type"].widget.attrs.update({"class": "form-control"})
        self.fields["address"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter address..."}
        )
        self.fields["city"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "City where property is located...",
            }
        )
        self.fields["google_maps"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Google map link..."}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["contact_info"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Contact number or email..."}
        )

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name =

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if not name:
            raise forms.ValidationError("Name is required", code="invalid")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if not description:
            raise forms.ValidationError("Description is required")
        return description

    def clean_type(self):
        type = self.cleaned_data.get("type")
        if not type:
            raise forms.ValidationError("Type is required")
        return type

    def clean_address(self):
        address = self.cleaned_data.get("address")
        if not address:
            raise forms.ValidationError("Address is required")
        return address

    def clean_city(self):
        city = self.cleaned_data.get("city")
        if not city:
            raise forms.ValidationError("City is required")
        return city

    def clean_google_maps(self):
        google_maps = self.cleaned_data.get("google_maps")
        return google_maps

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            raise forms.ValidationError("Image is required")
        return image

    def clean_contact_info(self):
        contact_info = self.changed_data.get("contact_info")
        if not contact_info:
            raise forms.ValidationError("Contact information is required")
        return contact_info
