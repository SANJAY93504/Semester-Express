from django.contrib import admin
from .models import LectureResource, CourseMaterial


@admin.register(LectureResource)
class LectureResourceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "lecture",
        "order",
        "is_published",
        "created_at",
    )

    list_filter = (
        "is_published",
        "lecture__unit__subject__course",
    )

    search_fields = (
        "title",
        "lecture__title",
        "lecture__unit__name",
        "lecture__unit__subject__name",
        "lecture__unit__subject__course__name",
    )

    ordering = (
        "lecture",
        "order",
        "title",
    )


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "course",
        "order",
        "is_published",
        "created_at",
    )

    list_filter = (
        "is_published",
        "course",
    )

    search_fields = (
        "title",
        "course__name",
    )

    ordering = (
        "course",
        "order",
        "title",
    )