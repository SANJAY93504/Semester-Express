from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from courses.views import home


urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "accounts/",
        include("allauth.urls")
    ),

    path(
        "dashboard/",
        include("dashboard.urls")
    ),

    path(
        "",
        home,
        name="home"
    ),

    path(
        "courses/",
        include("courses.urls")
    ),

    path(
        "payments/",
        include("payments.urls")
    ),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )