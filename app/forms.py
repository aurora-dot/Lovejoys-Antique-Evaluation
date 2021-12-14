from django import forms
from .models import EvaluationRequest


class EvaluationForm(forms.Form):
    class Meta:
        model = EvaluationRequest
        fields = ("comment", "contact_method")
