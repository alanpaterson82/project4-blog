from .models import TestimonialRequest
from django import forms


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = TestimonialRequest
        fields = ('name', 'email', 'message')