from django.db import models
from courses.models import Course, Subject, Unit, Lecture


class LectureResource(models.Model):
    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="resources"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True
    )

    pdf_file = models.FileField(
        upload_to="pdfs/",
        blank=True,
        null=True
    )

    resource_url = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title


class CourseMaterial(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="materials"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    pdf_file = models.FileField(
        upload_to="course-materials/",
        blank=True,
        null=True
    )

    resource_url = models.URLField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    is_published = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title