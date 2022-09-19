from django import forms

from .models import Property


class PostPropertyForm(forms.ModelForm):
    """
    Form to create a new Property.
    """

    class Meta:
        model = Property
        fields = [
            "name",
            "description",
            "image",
            "type",
            "address",
            "city",
            "google_maps",
            "contact_info",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter a name/title for property...",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Enter description. eg: 2BHK, 50 cent, 3 floors...",
            }
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
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
            {
                "class": "form-control",
                "placeholder": "Copy and paste link from google maps...",
            }
        )
        self.fields["contact_info"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Contact number or email..."}
        )
