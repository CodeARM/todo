from django import forms
from django.forms import ModelForm
import datetime
from .models import *


class TaskForm(forms.ModelForm):

    class Meta: 
        model = Task
        fields = '__all__'

class AreaForm(forms.ModelForm):

    class Meta: 
        model = Area
        fields = '__all__'

class ProjectForm(forms.ModelForm):

    class Meta: 
        model = Project
        fields = '__all__'