from django import forms
from .models import task

class taskform(forms.Form):
    class Meta:
        model = task
        field= __name__