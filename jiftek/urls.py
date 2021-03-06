"""jiftek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from django.http import HttpResponse
from django.conf.urls.static import static
from pages.views import (home_view, coming_soon_view,
                         about_us_view, team_and_facility_view, students_works_view,
                         xml_sitemap_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('about-us/', about_us_view, name="about-us"),
    path('services/', include('services.urls')),
    path('get-a-quote/', include('getQuote.urls')),
    # path('team-and-facility/', team_and_facility_view, name="team-and-facility"),
    path('team-and-facility/', about_us_view, name="team-and-facility"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
