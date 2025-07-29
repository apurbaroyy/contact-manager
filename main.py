import python_mysql as sq

db = sq.mysql_connect()
db.connect_db()
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),  # এখন root URL থেকে students.views.home এ যাবে
]

qq = input("Enter query")
output = db.execute_query(qq)
print("Available databases:")
for db_name in output:
    print("-", db_name[0])

#db.close_connection()
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_no = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
python manage.py makemigrations
python manage.py migrate

from django.contrib import admin
from .models import Student

admin.site.register(Student)
