from django.contrib import admin

from .models import (
    Collection,
    Course,
    Subject,
    Unit,
    Lecture,
)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "name",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "collection",
        "branch",
        "semester",
        "price",
        "is_paid",
        "is_active",
    )

    list_filter = (
        "is_paid",
        "is_active",
        "branch",
        "semester",
    )

    search_fields = (
        "name",
        "collection__name",
        "branch",
        "semester",
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "course",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "course",
    )

    search_fields = (
        "name",
        "course__name",
    )


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "subject",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
        "subject",
    )

    search_fields = (
        "name",
        "subject__name",
    )


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "unit",
        "order",
        "is_published",
        "created_at",
    )

    list_filter = (
        "is_published",
        "unit__subject__course",
    )

    search_fields = (
        "title",
        "unit__name",
        "unit__subject__name",
        "unit__subject__course__name",
    )