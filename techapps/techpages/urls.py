from django.urls import path
from django.utils.translation import gettext_lazy as _
from .views import (HomeTemplateView, ContactTemplateView, AboutTemplateView)

app_name = "techpages"

urlpatterns = [
    path("", view=HomeTemplateView.as_view(), name="home"),
    path("contact/", view=ContactTemplateView.as_view(), name="contact"),
    path("about/", view=AboutTemplateView.as_view(), name="about"),
]