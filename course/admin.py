from django.contrib import admin

from .models import course, Category

# Register your models here.

admin.site.register(course)
admin.site.register(Category)