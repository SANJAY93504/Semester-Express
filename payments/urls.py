from django.urls import path
from . import views


app_name = "payments"


urlpatterns = [
    path(
        "buy/<int:course_id>/",
        views.buy_course,
        name="buy_course"
    ),
]