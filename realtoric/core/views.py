from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from .forms import PostPropertyForm
from .models import Property


class PropertyListView(ListView):
    """
    Render properties for sale in home page.
    """

    model = Property
    context_object_name = "properties"
    queryset = Property.objects.filter(
        sale_status=Property.SaleStatus.FOR_SALE
    ).order_by("-created")[0:30]
    template_name = "pages/home.html"


property_list_view = PropertyListView.as_view()


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
