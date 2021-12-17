from django import forms

from .models import EvaluationRequest


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = EvaluationRequest
        fields = ("image", "item_description", "contact_method")
