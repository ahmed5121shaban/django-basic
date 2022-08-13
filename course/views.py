from django.shortcuts import render

from .models import course

# Create your views here.



def all_course(request):
    courses = course.objects.all()
    return render(request, 'course/course.html', {'ahmed':courses})

def single_course(request, id):
    course1 = course.objects.get(id=id)
    return render(request,'course/single.html', {'ahmed1':course1})