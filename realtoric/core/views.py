from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from .forms import PostPropertyForm


class PostPropertyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render a form to create a new Property.
    """

    form_class = PostPropertyForm
    template_name = "pages/add_property.html"
    success_url = reverse_lazy("core:post_property")
    success_message = _("Property posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


post_property_view = PostPropertyView.as_view()
