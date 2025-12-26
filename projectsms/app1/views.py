from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course, SimpleCourse
from .forms import StudentForm


def index(request):
    return render(request, "index.html")


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def view_students(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form, 'student': student})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'delete_student.html', {'student': student})

def delete_student_root(request):
    return redirect('view_students')

# Create your views here.


def simple_courses(request):
    # simple courses page removed — redirect to students list
    return redirect('view_students')


def student_courses(request, pk):
    # student courses template removed — redirect to students list
    return redirect('view_students')


def manage_enrollments(request, pk):
    # enrollment management UI removed — redirect to students list
    return redirect('view_students')
