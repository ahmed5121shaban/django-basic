
from django import forms
from .models import course

class CourseForm(forms.ModelForm):
    class Meta:
        model=course
        fields= ['title','content','salary','category']