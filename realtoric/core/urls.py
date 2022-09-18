from django.urls import path

from .views import post_property_view, property_list_view

app_name = "core"
urlpatterns = [
    path("", view=property_list_view, name="home"),
    path("post-property/", view=post_property_view, name="post_property"),
]
