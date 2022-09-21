from django import forms

from .models import Property


class PostPropertyForm(forms.ModelForm):
    """
    Form to create a new Property.
    """

    images = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "multiple": True}
        )
    )

    class Meta:
        model = Property
        fields = [
            "name",
            "description",
            "type",
            "address",
            "city",
            "google_maps",
            "contact_info",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a name for property...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a description. eg: 2BHK, 50 cent, 3 floors...",
                }
            ),
            "type": forms.Select(attrs={"class": "form-control"}),
            "address": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter address..."}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter city..."}
            ),
            "google_maps": forms.URLInput(
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

    field_order = [
        "name",
        "description",
        "type",
        "images",
        "address",
        "city",
        "google_maps",
        "contact_info",
    ]
