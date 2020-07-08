from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path

from .views import (cloud_services_view, 
                    web_and_app_view, 
                    it_consulting_view, 
                    security_and_compliance_view,
                    training_serevices_view
                    )

urlpatterns = [
    url(r'^cloud-computing/$', cloud_services_view, name="cloud-computing"),
    url(r'^web-and-app-design/$', web_and_app_view, name="web-and-app-design"),
    url(r'^it-consulting/$', it_consulting_view, name="it-consulting"),
    url(r'^security-and-compliance/$', security_and_compliance_view, name="security-and-compliance"),
    url(r'^training/$', training_serevices_view, name="training"),
]
