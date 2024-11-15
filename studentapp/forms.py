from django import forms
from django.shortcuts import redirect, render

from .models import StudentList


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']


