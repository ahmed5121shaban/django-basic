from django.shortcuts import render

from .models import course
# Create your views here.

def course(request):
    context = {'ahmed':'welcome'}
    return render(request, 'course/course.html', context)