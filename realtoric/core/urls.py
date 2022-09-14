from django.urls import path

from .views import post_property_view

app_name = "core"
urlpatterns = [
    path("post-property/", view=post_property_view, name="post_property"),
]
