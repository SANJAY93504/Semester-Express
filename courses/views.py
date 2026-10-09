from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Prefetch

from .models import Collection, Course, Subject, Unit, Lecture
from payments.models import Purchase


def home(request):

    collection_list = Collection.objects.filter(
        is_active=True
    )

    featured_courses = Course.objects.filter(
        is_active=True
    )[:6]

    free_courses = Course.objects.filter(
        is_active=True,
        is_paid=False
    )[:6]

    context = {
        "collections": collection_list,
        "featured_courses": featured_courses,
        "free_courses": free_courses,
    }

    return render(
        request,
        "index.html",
        context
    )


def paid_courses(request):

    courses = Course.objects.filter(
        is_active=True,
        is_paid=True
    )

    context = {
        "courses": courses,
    }

    return render(
        request,
        "courses/paid_courses.html",
        context
    )


def free_courses(request):

    courses = Course.objects.filter(
        is_active=True,
        is_paid=False
    )

    context = {
        "courses": courses,
    }

    return render(
        request,
        "courses/free_courses.html",
        context
    )


def collections(request):

    collection_list = Collection.objects.filter(
        is_active=True
    )

    context = {
        "collections": collection_list,
    }

    return render(
        request,
        "courses/collections.html",
        context
    )


def collection_detail(request, collection_id):

    collection = get_object_or_404(
        Collection,
        id=collection_id,
        is_active=True
    )

    courses = Course.objects.filter(
        collection=collection,
        is_active=True
    )

    context = {
        "collection": collection,
        "courses": courses,
    }

    return render(
        request,
        "courses/collection_detail.html",
        context
    )


def course_detail(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id,
        is_active=True
    )

    has_access = check_course_access(
        request,
        course
    )

    context = {
        "course": course,
        "has_access": has_access,
    }

    return render(
        request,
        "courses/course_detail.html",
        context
    )


def check_course_access(request, course):
    """
    Check whether the current user can access a course.
    """

    # Free course
    if not course.is_paid:
        return True

    # Paid course but user is not logged in
    if not request.user.is_authenticated:
        return False

    # Paid course and user has completed purchase
    return Purchase.objects.filter(
        user=request.user,
        course=course,
        payment_status="paid"
    ).exists()


def require_course_access(request, course):
    """
    Handle access rules for paid courses.
    """

    # Free course
    if not course.is_paid:
        return None

    # Paid course but user is not logged in
    if not request.user.is_authenticated:
        return redirect(
            f"/accounts/login/?next={request.path}"
        )

    # Paid course but not purchased
    if not check_course_access(request, course):
        messages.warning(
            request,
            "Please purchase this course to access its lectures."
        )

        return redirect(
            "courses:course_detail",
            course_id=course.id
        )

    return None


def course_learning(request, course_id):
    """
    Main learning page.

    Course
        -> Subject
            -> Unit
                -> Lecture
    """

    course = get_object_or_404(
        Course,
        id=course_id,
        is_active=True
    )

    # Check paid/free course access
    access_response = require_course_access(
        request,
        course
    )

    if access_response:
        return access_response

    # Get only active subjects,
    # active units,
    # and published lectures.
    subjects = Subject.objects.filter(
        course=course,
        is_active=True
    ).prefetch_related(
        Prefetch(
            "units",
            queryset=Unit.objects.filter(
                is_active=True
            ).prefetch_related(
                Prefetch(
                    "lectures",
                    queryset=Lecture.objects.filter(
                        is_published=True
                    )
                )
            )
        )
    )

    context = {
        "course": course,
        "subjects": subjects,
    }

    return render(
        request,
        "courses/course_learning.html",
        context
    )


def subject_detail(request, subject_id):

    subject = get_object_or_404(
        Subject,
        id=subject_id,
        is_active=True
    )

    course = subject.course

    access_response = require_course_access(
        request,
        course
    )

    if access_response:
        return access_response

    units = Unit.objects.filter(
        subject=subject,
        is_active=True
    )

    context = {
        "subject": subject,
        "units": units,
    }

    return render(
        request,
        "courses/subject_detail.html",
        context
    )


def unit_detail(request, unit_id):

    unit = get_object_or_404(
        Unit,
        id=unit_id,
        is_active=True
    )

    course = unit.subject.course

    access_response = require_course_access(
        request,
        course
    )

    if access_response:
        return access_response

    lectures = Lecture.objects.filter(
        unit=unit,
        is_published=True
    )

    context = {
        "unit": unit,
        "lectures": lectures,
    }

    return render(
        request,
        "courses/unit_detail.html",
        context
    )


def lecture_detail(request, lecture_id):

    lecture = get_object_or_404(
        Lecture,
        id=lecture_id,
        is_published=True
    )

    course = lecture.unit.subject.course

    access_response = require_course_access(
        request,
        course
    )

    if access_response:
        return access_response

    # Published lectures of the current unit
    unit_lectures = list(
        Lecture.objects.filter(
            unit=lecture.unit,
            is_published=True
        ).order_by(
            "order",
            "title"
        )
    )

    # Find current lecture position
    current_index = unit_lectures.index(lecture)

    previous_lecture = None
    next_lecture = None

    if current_index > 0:
        previous_lecture = unit_lectures[current_index - 1]

    if current_index < len(unit_lectures) - 1:
        next_lecture = unit_lectures[current_index + 1]

    resources = lecture.resources.filter(
        is_published=True
    )

    context = {
        "lecture": lecture,
        "resources": resources,
        "previous_lecture": previous_lecture,
        "next_lecture": next_lecture,
    }

    return render(
        request,
        "courses/lecture_detail.html",
        context
    )