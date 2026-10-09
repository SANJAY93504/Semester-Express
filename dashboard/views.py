from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import StudentProfileForm
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress

from payments.models import Purchase






@login_required
def dashboard(request):
    purchases = (
        Purchase.objects
        .filter(
            user=request.user,
            payment_status="paid"
        )
        .select_related("course")
    )

    context = {
        "purchases": purchases,
        "purchase_count": purchases.count(),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


@login_required
def profile(request):

    student_profile = getattr(
        request.user,
        "student_profile",
        None
    )

    if student_profile is None:
        from accounts.models import StudentProfile

        student_profile = StudentProfile.objects.create(
            user=request.user
        )

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=student_profile
        )

        if form.is_valid():
            form.save()

            return redirect("dashboard:profile")

    else:

        form = StudentProfileForm(
            instance=student_profile
        )

    # ==============================
    # GOOGLE ACCOUNT EMAIL
    # ==============================

    google_email = ""

    email_record = EmailAddress.objects.filter(
        user=request.user,
        verified=True
    ).first()

    if email_record:
        google_email = email_record.email

    if not google_email:
        google_email = request.user.email or ""

    if not google_email:
        google_account = SocialAccount.objects.filter(
            user=request.user,
            provider="google"
        ).first()

        if google_account:
            google_email = google_account.extra_data.get(
                "email",
                ""
            )

    context = {
        "student_profile": student_profile,
        "form": form,
        "google_email": google_email,
    }

    return render(
        request,
        "dashboard/profile.html",
        context
    )
    
@login_required
def edit_profile(request):

    student_profile = getattr(
        request.user,
        "student_profile",
        None
    )

    if student_profile is None:
        from accounts.models import StudentProfile

        student_profile = StudentProfile.objects.create(
            user=request.user
        )

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=student_profile
        )

        if form.is_valid():

            # Save Student Profile
            form.save()

            # Save User Name
            request.user.first_name = form.cleaned_data.get(
                "first_name",
                ""
            )

            request.user.last_name = form.cleaned_data.get(
                "last_name",
                ""
            )

            request.user.save(
                update_fields=[
                    "first_name",
                    "last_name"
                ]
            )

            return redirect("dashboard:profile")

    else:

        form = StudentProfileForm(
            instance=student_profile
        )

        # Existing name show in form
        form.fields["first_name"].initial = request.user.first_name
        form.fields["last_name"].initial = request.user.last_name

    google_email = request.user.email or ""

    context = {
        "student_profile": student_profile,
        "form": form,
        "google_email": google_email,
    }

    return render(
        request,
        "dashboard/edit_profile.html",
        context
    )
@login_required
def my_courses(request):

    purchases = (
        Purchase.objects
        .filter(
            user=request.user,
            payment_status="paid"
        )
        .select_related("course")
    )

    context = {
        "purchases": purchases,
    }

    return render(
        request,
        "dashboard/my_courses.html",
        context
    )
