from django.urls import path
from .views import all_course, single_course

urlpatterns = [
    path('', all_course, name='all_course'),
    path('course/<int:id>', single_course, name='single_course'),
]