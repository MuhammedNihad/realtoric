from django.urls import path

from .views import (
    post_property_view,
    property_detail_view,
    property_list_view,
    property_search_results_view,
)

app_name = "core"
urlpatterns = [
    path("", view=property_list_view, name="home"),
    path("search/", view=property_search_results_view, name="search_results"),
    path("property/<slug:slug>/", view=property_detail_view, name="property_detail"),
    path("post-property/", view=post_property_view, name="post_property"),
]
