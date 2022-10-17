from django.urls import path

from .views import (
    apartment_detail_view,
    apartment_post_view,
    apartment_update_view,
    choose_property_category_view,
    commercial_detail_view,
    commercial_post_view,
    commercial_update_view,
    house_detail_view,
    house_post_view,
    house_update_view,
    land_detail_view,
    land_post_view,
    land_update_view,
    property_list_view,
    property_search_results_view,
    villa_detail_view,
    villa_post_view,
    villa_update_view,
)

app_name = "core"
urlpatterns = [
    path("", view=property_list_view, name="home"),
    path("search/", view=property_search_results_view, name="search_results"),
    path("apartment/<slug:slug>/", view=apartment_detail_view, name="apartment_detail"),
    path(
        "apartment/<slug:slug>/update/",
        view=apartment_update_view,
        name="apartment_update",
    ),
    path(
        "commercial/<slug:slug>/", view=commercial_detail_view, name="commercial_detail"
    ),
    path(
        "commercial/<slug:slug>/update/",
        view=commercial_update_view,
        name="commercial_update",
    ),
    path("house/<slug:slug>/", view=house_detail_view, name="house_detail"),
    path("house/<slug:slug>/update/", view=house_update_view, name="house_update"),
    path("land/<slug:slug>/", view=land_detail_view, name="land_detail"),
    path("land/<slug:slug>/update/", view=land_update_view, name="land_update"),
    path("villa/<slug:slug>/", view=villa_detail_view, name="villa_detail"),
    path("villa/<slug:slug>/update/", view=villa_update_view, name="villa_update"),
    # Property posting related urls
    path("post/", view=choose_property_category_view, name="post"),
    path("post/apartment/", view=apartment_post_view, name="apartment_post"),
    path("post/commercial/", view=commercial_post_view, name="commercial_post"),
    path("post/house/", view=house_post_view, name="house_post"),
    path("post/land/", view=land_post_view, name="land_post"),
    path("post/villa/", view=villa_post_view, name="villa_post"),
]
