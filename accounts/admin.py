from django.contrib import admin
from .models import StudentProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "course",
        "branch",
        "semester",
        "student_id",
        "registration_date",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone_number",
        "student_id",
    )

    list_filter = (
        "course",
        "branch",
        "semester",
    )