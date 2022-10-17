from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    ApartmentPostForm,
    CommercialPostForm,
    HousePostForm,
    LandPostForm,
    VillaPostForm,
)
from .models import Apartment, Commercial, House, Land, SaleStatus, Villa


class ChoosePropertyCategoryView(LoginRequiredMixin, TemplateView):
    """
    Render page for choosing the type/category of property to post.
    """

    template_name = "pages/choose_property_category.html"


choose_property_category_view = ChoosePropertyCategoryView.as_view()


class ApartmentPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render form to create a new Apartment.
    """

    form_class = ApartmentPostForm
    template_name = "pages/post_property.html"
    success_url = reverse_lazy("core:apartment_post")
    success_message = _("Apartment posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        apartment_data = form.save()
        print("aprtdata", apartment_data)

        # Save the apartment's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.apartment_images.create(apartment=apartment_data, image=image)
        return super().form_valid(form)


apartment_post_view = ApartmentPostView.as_view()


class CommercialPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render form to create a new Commercial property.
    """

    form_class = CommercialPostForm
    template_name = "pages/post_property.html"
    success_url = reverse_lazy("core:commercial_post")
    success_message = _("Commercial property posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        commercial_data = form.save()

        # Save the commercial properties's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.commercial_images.create(
                commercial=commercial_data, image=image
            )
        return super().form_valid(form)


commercial_post_view = CommercialPostView.as_view()


class HousePostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render form to create a new House.
    """

    form_class = HousePostForm
    template_name = "pages/post_property.html"
    success_url = reverse_lazy("core:house_post")
    success_message = _("House posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        house_data = form.save()

        # Save the house's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.house_images.create(house=house_data, image=image)
        return super().form_valid(form)


house_post_view = HousePostView.as_view()


class LandPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render form to create a new Land.
    """

    form_class = LandPostForm
    template_name = "pages/post_property.html"
    success_url = reverse_lazy("core:land_post")
    success_message = _("Land posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        land_data = form.save()

        # Save the land's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.land_images.create(land=land_data, image=image)
        return super().form_valid(form)


land_post_view = LandPostView.as_view()


class VillaPostView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Render form to create a new Villa.
    """

    form_class = VillaPostForm
    template_name = "pages/post_property.html"
    success_url = reverse_lazy("core:villa_post")
    success_message = _("Villa posted successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        villa_data = form.save()

        # Save the villa's images
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.villa_images.create(villa=villa_data, image=image)
        return super().form_valid(form)


villa_post_view = VillaPostView.as_view()


class AllPropertyListView(ListView):
    """
    Render properties for sale in home page.
    """

    model = Apartment
    context_object_name = "apartments"
    queryset = Apartment.objects.filter(sale_status=SaleStatus.FOR_SALE).order_by(
        "-listed_on"
    )
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["commercials"] = Commercial.objects.filter(
            sale_status=SaleStatus.FOR_SALE
        ).order_by("-listed_on")
        context["houses"] = House.objects.filter(
            sale_status=SaleStatus.FOR_SALE
        ).order_by("-listed_on")
        context["lands"] = Land.objects.filter(
            sale_status=SaleStatus.FOR_SALE
        ).order_by("-listed_on")
        context["villas"] = Villa.objects.filter(
            sale_status=SaleStatus.FOR_SALE
        ).order_by("-listed_on")
        return context


property_list_view = AllPropertyListView.as_view()


class PropertySearchResultsView(ListView):
    """
    Render search results.
    """

    pass
    # model = Property
    # context_object_name = "properties"
    # template_name = "pages/search_results.html"

    # def get_queryset(self):
    #     """
    #     Return search results.
    #     """

    #     query = self.request.GET.get("search")
    #     return Property.objects.filter(
    #         Q(name__icontains=query)
    #         | Q(description__icontains=query)
    #         | Q(address__icontains=query)
    #         | Q(city__icontains=query)
    #     ).order_by("-created")


property_search_results_view = PropertySearchResultsView.as_view()


class ApartmentDetailView(DetailView):
    """
    Render apartment details.
    """

    model = Apartment
    context_object_name = "apartment"
    template_name = "pages/property_detail.html"


apartment_detail_view = ApartmentDetailView.as_view()


class CommercialDetailView(DetailView):
    """
    Render commercial details.
    """

    model = Commercial
    context_object_name = "commercial"
    template_name = "pages/property_detail.html"


commercial_detail_view = CommercialDetailView.as_view()


class HouseDetailView(DetailView):
    """
    Render house details.
    """

    model = House
    context_object_name = "house"
    template_name = "pages/property_detail.html"


house_detail_view = HouseDetailView.as_view()


class LandDetailView(DetailView):
    """
    Render land details.
    """

    model = Land
    context_object_name = "land"
    template_name = "pages/property_detail.html"


land_detail_view = LandDetailView.as_view()


class VillaDetailView(DetailView):
    """
    Render villa details.
    """

    model = Villa
    context_object_name = "villa"
    template_name = "pages/property_detail.html"


villa_detail_view = VillaDetailView.as_view()


class ApartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update an apartment.
    """

    model = Apartment
    form_class = ApartmentPostForm
    template_name = "pages/post_property.html"
    success_message = _("Apartment updated successfully")

    def get_success_url(self):
        return reverse("core:apartment_detail", kwargs={"slug": self.object.slug})


apartment_update_view = ApartmentUpdateView.as_view()


class CommercialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update a commercial.
    """

    model = Commercial
    form_class = CommercialPostForm
    template_name = "pages/post_property.html"
    success_message = _("Commercial updated successfully")

    def get_success_url(self):
        return reverse("core:commercial_detail", kwargs={"slug": self.object.slug})


commercial_update_view = CommercialUpdateView.as_view()


class HouseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update a house.
    """

    model = House
    form_class = HousePostForm
    template_name = "pages/post_property.html"
    success_message = _("House updated successfully")

    def get_success_url(self):
        return reverse("core:house_detail", kwargs={"slug": self.object.slug})


house_update_view = HouseUpdateView.as_view()


class LandUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update a land.
    """

    model = Land
    form_class = LandPostForm
    template_name = "pages/post_property.html"
    success_message = _("Land updated successfully")

    def get_success_url(self):
        return reverse("core:land_detail", kwargs={"slug": self.object.slug})


land_update_view = LandUpdateView.as_view()


class VillaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update a villa.
    """

    model = Villa
    form_class = VillaPostForm
    template_name = "pages/post_property.html"
    success_message = _("Villa updated successfully")

    def get_success_url(self):
        return reverse("core:villa_detail", kwargs={"slug": self.object.slug})


villa_update_view = VillaUpdateView.as_view()
