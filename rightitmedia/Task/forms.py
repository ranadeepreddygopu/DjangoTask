from django import forms
from Task.models import Task
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
