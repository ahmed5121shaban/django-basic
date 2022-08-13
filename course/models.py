from django.db import models

# Create your models here.
class course(models.Model):
    title = models.CharField(max_length=100)
    imag = models.ImageField(upload_to = 'coursephoto/%y/%m/%d')
    content = models.TextField(max_length=1000)
    salary = models.DecimalField(max_digits=10, decimal_places=1)



    def __str__(self) -> str:
        return self.title