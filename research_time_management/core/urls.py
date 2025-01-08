from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name="student"),  # Hiển thị bảng Sinh viên
    path('lecturers/', views.lecturers, name="lecturers"),  # Hiển thị bảng Giảng viên
    path('register/', views.register, name='register'),  # Đăng ký
    path('login/', views.loginPage, name='login'),  # Đăng ký
    path('logout/', views.logoutPage, name='logout'),  # Đường dẫn đăng xuất
    path('lecturers/add/', views.add_lecturer, name='add_lecturer'),
    path('lecturers/edit/<int:id>/', views.edit_lecturer, name='edit_lecturer'),  # Trang chỉnh sửa giảng viên
    path('lecturers/delete/<int:id>/', views.delete_lecturer, name='delete_lecturer'),  # Xóa giảng viên
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),  # Trang chỉnh sửa giảng viên
    path('student/delete/<int:id>/', views.delete_student, name='delete_student'),  # Xóa giảng viên
    path('search/', views.search, name='search'),
    
]

    
