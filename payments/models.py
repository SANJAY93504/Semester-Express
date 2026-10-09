from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Purchase(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="purchases"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="purchases"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS_CHOICES,
        default="pending"
    )

    razorpay_order_id = models.CharField(
        max_length=200,
        blank=True
    )

    razorpay_payment_id = models.CharField(
        max_length=200,
        blank=True
    )

    razorpay_signature = models.CharField(
        max_length=500,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.course.name} - {self.payment_status}"