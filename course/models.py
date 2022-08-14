from urllib import request
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class course(models.Model):
    outher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_course')
    title = models.CharField(max_length=100)
    imag = models.ImageField(upload_to = 'coursephoto/%y/%m/%d')
    content = models.TextField(max_length=1000)
    salary = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category_course')

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name