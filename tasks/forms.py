from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    class Meta: 
        model = Task
        fields = '__all__'

class AreaForm(forms.ModelForm):

    class Meta: 
        model = Area
        fields = '__all__'