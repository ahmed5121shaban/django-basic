from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_course, name='all_course'),
    path('new/', views.new_course, name='new_course'),
    path('<int:id>/', views.single_course, name='single_course'),
    path('<int:id>/edit', views.edit_course, name='edit_course'),
    path('<int:id>/delete', views.delete_course, name='delete_course'),
]