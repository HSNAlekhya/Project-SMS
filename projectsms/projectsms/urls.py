"""projectsms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import (
    index,
    add_student,
    view_students,
    update_student,
    delete_student,
    delete_student_root,
    student_courses,
    manage_enrollments,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('add_student/', add_student, name='add_student'),
    path('view_students/', view_students, name='view_students'),
    path('update_student/<int:pk>/', update_student, name='update_student'),
    path('delete_student/<int:pk>/', delete_student, name='delete_student'),
    path('delete_student/', delete_student_root, name='delete_student_root'),
    path('student/<int:pk>/courses/', student_courses, name='student_courses'),

]
