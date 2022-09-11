from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }


class UserSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    name = forms.CharField(
        max_length=255,
        label=_("Name"),
        widget=forms.TextInput(attrs={"placeholder": _("Name")}),
    )
    address = forms.CharField(
        max_length=255,
        label=_("Address"),
        required=False,
        widget=forms.Textarea(attrs={"placeholder": _("Enter your address here...")}),
    )
    phone = forms.CharField(
        max_length=13,
        label=_("Phone Number"),
        widget=forms.TextInput(
            attrs={"placeholder": _("Phone Number"), "type": "number"}
        ),
    )

    def save(self, request):
        user = super().save(request)
        user.name = self.cleaned_data["name"]
        user.address = self.cleaned_data["address"]
        user.phone = self.cleaned_data["phone"]
        user.save()
        return user


class UserSocialSignupForm(SocialSignupForm):
    """
    Renders the form when user has signed up using social accounts.
    Default fields will be added automatically.
    See UserSignupForm otherwise.
    """
