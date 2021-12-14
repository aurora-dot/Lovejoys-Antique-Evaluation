from django import forms
from .models import EvaluationRequest


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = EvaluationRequest
        fields = ("item_description", "contact_method")
