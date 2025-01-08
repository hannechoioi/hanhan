from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
    
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)  # Mã số sinh viên
    full_name = models.CharField(max_length=100)  # Họ tên
    class_code = models.CharField(max_length=10)  # Mã lớp
    time_spent = models.IntegerField()  # Thời gian nghiên cứu (tính theo giờ)

    def __str__(self):
        return self.full_name

class Lecturer(models.Model):
    lecturer_id = models.CharField(max_length=20, unique=True)  # Mã số giảng viên
    full_name = models.CharField(max_length=100)  # Họ tên
    class_code = models.CharField(max_length=10)  # Mã lớp
    
    time_spent = models.IntegerField()  # Thời gian nghiên cứu (tính theo giờ)

    def __str__(self):
        return self.full_name

#Thay doi form
class CreateUserFrm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']