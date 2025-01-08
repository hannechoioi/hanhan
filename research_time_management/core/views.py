from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Lecturer
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
from django.utils.dateparse import parse_datetime
from django.utils import timezone


def home(request):
    return render(request, 'core/home1.html')


def students(request):
    students_list = Student.objects.all()  # Lấy tất cả Sinh viên từ cơ sở dữ liệu
    return render(request, 'core/students.html', {'students': students_list})

def lecturers(request):
    lecturers_list = Lecturer.objects.all()  # Lấy tất cả Giảng viên từ cơ sở dữ liệu
    return render(request, 'core/lecturers.html', {'lecturers': lecturers_list})
def register(request):
    form = CreateUserFrm()
    
    if request.method == "POST":
       form = CreateUserFrm(request.POST)
       if form.is_valid():
          form.save()
          messages.info(request, 'Đăng ký tài khoản thành công!')
    context ={'form':form}
    
    return render(request, 'core/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        user1 = authenticate(username =username1, password =password1)
        if user1 is not None:
            login(request, user1)
            return redirect("home")
        else: messages.info(request, 'tên đăng nhập hoặc mật khẩu chưa đúng!')
    context = {}
    return render(request, 'core/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')

def add_lecturer(request):
    # Logic để thêm giảng viên (ví dụ: hiển thị form)
    return render(request, 'core/add_lecturer.html')

def add_lecturer(request):
    if request.method == "POST":
        lecturer_id = request.POST['lecturer_id']
        full_name = request.POST['full_name']
        
        time_start = parse_datetime(request.POST['time_start'])
        time_end = parse_datetime(request.POST['time_end'])

        # Tính toán tổng thời gian
        time_spent = (time_end - time_start).total_seconds() / 3600  # Tính theo giờ

        # Lưu vào cơ sở dữ liệu
        Lecturer.objects.create(
            lecturer_id=lecturer_id,
            full_name=full_name,
           
        
            time_spent=time_spent
        )

        # Chuyển hướng đến trang danh sách giảng viên
        return redirect('lecturers')

    return render(request, 'core/add_lecturer.html')

def edit_lecturer(request, id):
    lecturer = get_object_or_404(Lecturer, id=id)

    if request.method == 'POST':
        lecturer.lecturer_id = request.POST.get('lecturer_id')
        lecturer.full_name = request.POST.get('full_name')
        lecturer.class_code = request.POST.get('class_code')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')

        # Chuyển đổi thời gian bắt đầu và kết thúc
        time_start = timezone.datetime.strptime(time_start, '%Y-%m-%dT%H:%M')
        time_end = timezone.datetime.strptime(time_end, '%Y-%m-%dT%H:%M')

        # Tính toán tổng thời gian
        lecturer.time_start = time_start
        lecturer.time_end = time_end
        lecturer.time_spent = (time_end - time_start).total_seconds() / 3600  # tính tổng giờ

        lecturer.save()

        return redirect('lecturers')  # Sau khi chỉnh sửa, chuyển về danh sách giảng viên

    return render(request, 'core/edit_lecturer.html', {'lecturer': lecturer})


def delete_lecturer(request, id):
    lecturer = get_object_or_404(Lecturer, id=id)
    if request.method == 'POST':
        lecturer.delete()  # Xóa giảng viên khỏi cơ sở dữ liệu
        messages.success(request, "Xóa thành công!") 
        return redirect('lecturers')  # Sau khi xóa, chuyển về trang danh sách

    return render(request, 'core/delete_lecturer.html', {'lecturer': lecturer})


    

    
def add_student(request):
    if request.method == "POST":
        student_id = request.POST['student_id']
        full_name = request.POST['full_name']
        class_code = request.POST['class_code']
        time_start = parse_datetime(request.POST['time_start'])
        time_end = parse_datetime(request.POST['time_end'])

        # Tính toán tổng thời gian
        time_spent = (time_end - time_start).total_seconds() / 3600  # Tính theo giờ

        # Lưu vào cơ sở dữ liệu
        Student.objects.create(
            student_id=student_id,
            full_name=full_name,
            class_code=class_code,
        
            time_spent=time_spent
        )

        # Chuyển hướng đến trang danh sách giảng viên
        return redirect('student')

    return render(request, 'core/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.lecturer_id = request.POST.get('lecturer_id')
        student.full_name = request.POST.get('full_name')
        student.class_code = request.POST.get('class_code')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')

        # Chuyển đổi thời gian bắt đầu và kết thúc
        time_start = timezone.datetime.strptime(time_start, '%Y-%m-%dT%H:%M')
        time_end = timezone.datetime.strptime(time_end, '%Y-%m-%dT%H:%M')

        # Tính toán tổng thời gian
        student.time_start = time_start
        student.time_end = time_end
        student.time_spent = (time_end - time_start).total_seconds() / 3600  # tính tổng giờ

        student.save()

        return redirect('student')  # Sau khi chỉnh sửa, chuyển về danh sách giảng viên

    return render(request, 'core/edit_student.html', {'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()  # Xóa giảng viên khỏi cơ sở dữ liệu
        messages.success(request, "Xóa thành công!") 
        return redirect('student')  # Sau khi xóa, chuyển về trang danh sách

    return render(request, 'core/delete_student.html', {'student': student})

def search(request):
    query = request.GET.get('q', '')  # Lấy giá trị tìm kiếm từ GET request

    if query:
        # Tìm kiếm giảng viên theo mã số
        lecturers = Lecturer.objects.filter(lecturer_id__icontains=query)
        # Tìm kiếm sinh viên theo mã số
        student = Student.objects.filter(student_id__icontains=query)
    else:
        lecturers = Lecturer.objects.none()  # Nếu không có tìm kiếm, trả về danh sách rỗng
        student = Student.objects.none()  # Tương tự với sinh viên

    return render(request, 'core/search_results.html', {'lecturers': lecturers, 'student': student, 'query': query})