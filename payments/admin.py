from django.contrib import admin
from .models import Purchase


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "course",
        "amount",
        "payment_status",
        "razorpay_order_id",
        "razorpay_payment_id",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__email",
        "course__name",
        "razorpay_order_id",
        "razorpay_payment_id",
    )

    list_filter = (
        "payment_status",
        "course",
        "created_at",
    )

    readonly_fields = (
        "razorpay_order_id",
        "razorpay_payment_id",
        "razorpay_signature",
        "created_at",
        "updated_at",
    )