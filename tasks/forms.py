from pyexpat import model
from django import forms
from .models import Tasks


class Taskforms(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
