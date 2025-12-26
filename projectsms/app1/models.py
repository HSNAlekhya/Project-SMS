from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_no = models.CharField(max_length=20, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    courses = models.ManyToManyField('Course', blank=True, related_name='students')
    # simple_courses: optional simple list of course names (max 50 chars)
    simple_courses = models.ManyToManyField('SimpleCourse', blank=True, related_name='students')
    # optional single-text course field
    course_name = models.CharField(max_length=50, blank=True)
    # single selected course shown as a dropdown in the form
    selected_course = models.ForeignKey(
        'SimpleCourse', null=True, blank=True, on_delete=models.SET_NULL, related_name='selected_students'
    )
    # attendance percentage (0-100)
    attendance = models.PositiveIntegerField(null=True, blank=True, help_text='Attendance percentage (0-100)')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_no})"


class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    credits = models.PositiveIntegerField(default=3)
    instructor = models.CharField(max_length=100, blank=True)
    semester = models.CharField(max_length=20, blank=True)
    fee = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.title} ({self.code})"


class SimpleCourse(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
