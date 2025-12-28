from django.contrib import admin
from .models import Student, Course, SimpleCourse


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'roll_no', 'email', 'age', 'gender', 'attendance','grade','fee_status',)
	filter_horizontal = ('courses','simple_courses',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'credits', 'instructor', 'semester',)


@admin.register(SimpleCourse)
class SimpleCourseAdmin(admin.ModelAdmin):
    list_display = ('name',)



