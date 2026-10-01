from django import forms

from .models import AdoptionRequest


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = [
            "phone",
            "address",
            "reason",
            "previous_pet_experience",
            "message",
        ]

        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter your phone number",
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Enter your full address",
                }
            ),
            "reason": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Why would you like to adopt this pet?",
                }
            ),
            "previous_pet_experience": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Any additional information?",
                }
            ),
        }

        labels = {
            "previous_pet_experience": "I have previous experience with pets",
            "message": "Additional Message",
        }