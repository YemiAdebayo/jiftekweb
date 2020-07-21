from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path

from .views import register_view
from pages.views import coming_soon_view

urlpatterns = [
    # url(r'', register_view, name="register"),
    url(r'', coming_soon_view, name="register"),
]
