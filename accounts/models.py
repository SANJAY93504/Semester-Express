from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    profile_photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    course = models.CharField(
        max_length=150,
        blank=True
    )

    branch = models.CharField(
        max_length=150,
        blank=True
    )

    semester = models.CharField(
        max_length=50,
        blank=True
    )

    student_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    registration_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username