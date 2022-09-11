from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from .forms import PostPropertyForm

# from django.urls import reverse


class PostPropertyView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render a form to create a new Property.
    """

    form_class = PostPropertyForm
    template_name = "pages/add_property.html"
    success_url = "/post-property/"
    success_message = _("Property posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("core:property_detail", kwargs={"pk": self.object.pk})


post_property_view = PostPropertyView.as_view()
