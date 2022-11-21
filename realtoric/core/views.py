from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    FormView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import (
    ApartmentPostForm,
    CommercialPostForm,
    HousePostForm,
    LandPostForm,
    SearchForm,
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


class AllPropertyListView(ListView, FormView):
    """
    Render properties for sale in home page.
    """

    model = Apartment
    context_object_name = "apartments"
    queryset = Apartment.objects.filter(sale_status=SaleStatus.FOR_SALE).order_by(
        "-listed_on"
    )
    template_name = "pages/home.html"
    form_class = SearchForm

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


class PropertySearchResultsView(ListView, FormView):
    """
    Render search results.
    """

    context_object_name = "properties"
    template_name = "pages/search_results.html"
    form_class = SearchForm

    def get_queryset(self):
        """
        Return search results.
        """

        city = self.request.GET.get("city", None)
        category = self.request.GET.get("category", None)

        if city and category:
            if category == "Apartment":
                apartment = Apartment.objects.filter(Q(city__icontains=city))
                return apartment

            elif category == "Commercial":
                commercial = Commercial.objects.filter(Q(city__icontains=city))
                return commercial

            elif category == "House":
                house = House.objects.filter(Q(city__icontains=city))
                return house

            elif category == "Land":
                land = Land.objects.filter(Q(city__icontains=city))
                return land

            elif category == "Villa":
                villa = Villa.objects.filter(Q(city__icontains=city))
                return villa
        else:
            messages.error(self.request, _("Something went wrong."))


property_search_results_view = PropertySearchResultsView.as_view()


class ApartmentDetailUpdateView(UpdateView):
    """
    Render apartment details along with update mark as sold and delete.
    """

    model = Apartment
    fields = ["sale_status"]
    context_object_name = "apartment"
    template_name = "pages/property_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            if request.user == self.object.user:
                if "sold" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("Apartment marked as sold"))
                    return redirect("core:apartment_detail", slug=self.object.slug)

                if "delete" in request.POST:
                    self.object.delete()
                    messages.success(request, _("Apartment deleted"))
                    return redirect("core:home")
            else:
                messages.error(
                    request, _("You are not authorized to perform this action")
                )
        except Exception:
            messages.error(request, _("Something went wrong"))


apartment_detail_view = ApartmentDetailUpdateView.as_view()


class CommercialDetailUpdateView(UpdateView):
    """
    Render commercial details along with update mark as sold and delete.
    """

    model = Commercial
    fields = ["sale_status"]
    context_object_name = "commercial"
    template_name = "pages/property_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            if request.user == self.object.user:
                if "sold" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("Commercial marked as sold"))
                    return redirect("core:commercial_detail", slug=self.object.slug)

                if "delete" in request.POST:
                    self.object.delete()
                    messages.success(request, _("Commercial deleted"))
                    return redirect("core:home")
            else:
                messages.error(
                    request, _("You are not authorized to perform this action")
                )
        except Exception:
            messages.error(request, _("Something went wrong"))


commercial_detail_view = CommercialDetailUpdateView.as_view()


class HouseDetailUpdateView(UpdateView):
    """
    Render house details along with update mark as sold and delete.
    """

    model = House
    fields = ["sale_status"]
    context_object_name = "house"
    template_name = "pages/property_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            if request.user == self.object.user:
                if "sold" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("House marked as sold"))
                    return redirect("core:house_detail", slug=self.object.slug)

                if "delete" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("House deleted"))
                    return redirect("core:home")
            else:
                messages.error(
                    request, _("You are not authorized to perform this action")
                )
        except Exception:
            messages.error(request, _("Something went wrong"))


house_detail_view = HouseDetailUpdateView.as_view()


class LandDetailUpdateView(UpdateView):
    """
    Render land details along with update mark as sold and delete.
    """

    model = Land
    fields = ["sale_status"]
    context_object_name = "land"
    template_name = "pages/property_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            if request.user == self.object.user:
                if "sold" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("Land marked as sold"))
                    return redirect("core:land_detail", slug=self.object.slug)

                if "delete" in request.POST:
                    self.object.delete()
                    messages.success(request, _("Land deleted"))
                    return redirect("core:home")
            else:
                messages.error(
                    request, _("You are not authorized to perform this action")
                )
        except Exception:
            messages.error(request, _("Something went wrong"))


land_detail_view = LandDetailUpdateView.as_view()


class VillaDetailUpdateView(UpdateView):
    """
    Render villa details along with update mark as sold and delete.
    """

    model = Villa
    fields = ["sale_status"]
    context_object_name = "villa"
    template_name = "pages/property_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            if request.user == self.object.user:
                if "sold" in request.POST:
                    self.object.sale_status = SaleStatus.SOLD
                    self.object.save()
                    messages.success(request, _("Villa marked as sold"))
                    return redirect("core:villa_detail", slug=self.object.slug)

                if "delete" in request.POST:
                    self.object.delete()
                    messages.success(request, _("Villa deleted"))
                    return redirect("core:home")
            else:
                messages.error(
                    request, _("You are not authorized to perform this action")
                )
        except Exception:
            messages.error(request, _("Something went wrong"))


villa_detail_view = VillaDetailUpdateView.as_view()


class ApartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Render form to update an apartment.
    """

    model = Apartment
    form_class = ApartmentPostForm
    template_name = "pages/post_property.html"
    success_message = _("Apartment updated successfully")

    def form_valid(self, form):
        form.instance.user = self.request.user
        apartment_data = form.save()

        # Delete existing images of the apartment instance
        for old_image in form.instance.apartment_images.all():
            old_image.delete()

        # Create new apartment images for the instance
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.apartment_images.create(apartment=apartment_data, image=image)
        return super().form_valid(form)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        commercial_data = form.save()

        # Delete existing images of the commercial instance
        for old_image in form.instance.commercial_images.all():
            old_image.delete()

        # Create new commercial images for the instance
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.commercial_images.create(
                commercial=commercial_data, image=image
            )
        return super().form_valid(form)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        house_data = form.save()

        # Delete existing images of the house instance
        for old_image in form.instance.house_images.all():
            old_image.delete()

        # Create new house images for the instance
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.house_images.create(house=house_data, image=image)
        return super().form_valid(form)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        land_data = form.save()

        # Delete existing images of the land instance
        for old_image in form.instance.land_images.all():
            old_image.delete()

        # Create new land images for the instance
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.land_images.create(land=land_data, image=image)
        return super().form_valid(form)

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        villa_data = form.save()

        # Delete existing images of the villa instance
        for old_image in form.instance.villa_images.all():
            old_image.delete()

        # Create new villa images for the instance
        images = self.request.FILES.getlist("images")
        for image in images:
            form.instance.villa_images.create(villa=villa_data, image=image)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("core:villa_detail", kwargs={"slug": self.object.slug})


villa_update_view = VillaUpdateView.as_view()
