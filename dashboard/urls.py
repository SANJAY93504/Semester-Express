from django.urls import path

from .views import (
    dashboard,
    profile,
    edit_profile,
    my_courses,
)


app_name = "dashboard"


urlpatterns = [

    path(
        "",
        dashboard,
        name="home"
    ),

    path(
        "profile/",
        profile,
        name="profile"
    ),

    path(
        "profile/edit/",
        edit_profile,
        name="edit_profile"
    ),

    path(
        "my-courses/",
        my_courses,
        name="my_courses"
    ),

]