from django.db import models

# Create your models here.
class Student(models.Model):
        created_at = models.DateTimeField(auto_now_add=True)
        first_name = models.CharField(max_length=50)
        last_name =  models.CharField(max_length=50)
        email =  models.CharField(max_length=100)
        age = models.IntegerField()
        gender =  models.CharField(max_length=100)
        def __str__(self):
            return f'{self.first_name} {self.last_name}'
        