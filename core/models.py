from django.db import models

# Create your models here.

class Student(models.Model):
    reg_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    email = models.CharField(max_length=255)
    

    def __str__(self):
        return self.first_name

    