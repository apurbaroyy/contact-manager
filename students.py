from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_no = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.contrib import admin
from .models import Student

admin.site.register(Student)
INSTALLED_APPS = [
    ...
    'students',
]
from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Django is working! This is the home page.")
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
