from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your first name",
            }
        )
    )

    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your last name",
            }
        )
    )

    class Meta:
        model = StudentProfile

        fields = [
            "profile_photo",
            "phone_number",
            "course",
            "branch",
            "semester",
            "student_id",
        ]

        widgets = {
            "phone_number": forms.TextInput(
                attrs={
                    "placeholder": "Enter phone number",
                }
            ),

            "course": forms.TextInput(
                attrs={
                    "placeholder": "Enter course",
                }
            ),

            "branch": forms.TextInput(
                attrs={
                    "placeholder": "Enter branch",
                }
            ),

            "semester": forms.TextInput(
                attrs={
                    "placeholder": "Enter semester",
                }
            ),

            "student_id": forms.TextInput(
                attrs={
                    "placeholder": "Enter student ID",
                }
            ),
        }