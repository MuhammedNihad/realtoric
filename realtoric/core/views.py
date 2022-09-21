from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, ListView

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
    ).order_by("-created")
    template_name = "pages/home.html"


property_list_view = PropertyListView.as_view()


class PropertySearchResultsView(ListView):
    """
    Render search results.
    """

    model = Property
    context_object_name = "properties"
    template_name = "pages/search_results.html"

    def get_queryset(self):
        """
        Return search results.
        """

        query = self.request.GET.get("search")
        return Property.objects.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(address__icontains=query)
            | Q(city__icontains=query)
        ).order_by("-created")


property_search_results_view = PropertySearchResultsView.as_view()


class PropertyDetailView(DetailView):
    """
    Render property details.
    """

    model = Property
    context_object_name = "property"
    template_name = "pages/property_detail.html"


property_detail_view = PropertyDetailView.as_view()


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
        property_data = form.save()

        # Save the property's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.images.create(property=property_data, image=image)
        return super().form_valid(form)


post_property_view = PostPropertyView.as_view()
