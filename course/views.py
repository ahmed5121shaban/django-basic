from django.shortcuts import render, redirect

from .forms import CourseForm

from .models import course

# Create your views here.


# all courses
def all_course(request):
    courses = course.objects.all()
    return render(request, 'course/course.html', {'ahmed':courses})

# single courses
def single_course(request, id):
    course1 = course.objects.get(id=id)
    return render(request,'course/single.html', {'ahmed1':course1})

# add new courses
def new_course(request):
    if request.method == 'POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.outher = request.user
            myform.save()
    else:
        form=CourseForm()
    return render(request,'course/new.html',{'form':form})


# edite courses
def edit_course(request,id):
    course1 = course.objects.get(id=id)
    if request.method == 'POST':
        form=CourseForm(request.POST,instance=course1)
        if form.is_valid():
            form.save()
    else:
        form=CourseForm(instance=course1)
    return render(request,'course/edit.html',{'form':form})

# delet courses
def delete_course(request,id):
    course1 = course.objects.get(id=id)
    course1.delete()
    return redirect('/course/')
