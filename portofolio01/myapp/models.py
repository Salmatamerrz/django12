from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()



class Course(models.Model):
    coursename = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    coursenumber = models.IntegerField()

class Post(models.Model):
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
        )

    username = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=Male)
    time = models.DateTimeField(auto_now_add=True)


