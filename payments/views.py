from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings

import razorpay

from courses.models import Course
from .models import Purchase


@login_required
def buy_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        is_active=True
    )

    existing_purchase = Purchase.objects.filter(
        user=request.user,
        course=course,
        payment_status="paid"
    ).first()

    if existing_purchase:
        return redirect(
            "courses:course_detail",
            course_id=course.id
        )

    purchase = Purchase.objects.create(
        user=request.user,
        course=course,
        amount=course.price,
        payment_status="pending",
    )

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET,
        )
    )

    amount_paise = int(course.price * 100)

    razorpay_order = client.order.create(
        data={
            "amount": amount_paise,
            "currency": "INR",
            "receipt": f"purchase_{purchase.id}",
        }
    )

    purchase.razorpay_order_id = razorpay_order["id"]
    purchase.save(
        update_fields=["razorpay_order_id"]
    )

    context = {
        "course": course,
        "purchase": purchase,
        "razorpay_order_id": razorpay_order["id"],
        "razorpay_key_id": settings.RAZORPAY_KEY_ID,
    }

    return render(
        request,
        "payments/checkout.html",
        context
    )