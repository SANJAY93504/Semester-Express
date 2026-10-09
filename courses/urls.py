from django.urls import path
from . import views


app_name = "courses"


urlpatterns = [

    path(
        "",
        views.collections,
        name="collections"
    ),

    path(
        "paid/",
        views.paid_courses,
        name="paid_courses"
    ),

    path(
        "free/",
        views.free_courses,
        name="free_courses"
    ),

    path(
        "collection/<int:collection_id>/",
        views.collection_detail,
        name="collection_detail"
    ),

    path(
        "course/<int:course_id>/",
        views.course_detail,
        name="course_detail"
    ),

    # Course learning page
    path(
        "course/<int:course_id>/learn/",
        views.course_learning,
        name="course_learning"
    ),

    path(
        "subject/<int:subject_id>/",
        views.subject_detail,
        name="subject_detail"
    ),

    path(
        "unit/<int:unit_id>/",
        views.unit_detail,
        name="unit_detail"
    ),

    path(
        "lecture/<int:lecture_id>/",
        views.lecture_detail,
        name="lecture_detail"
    ),

]