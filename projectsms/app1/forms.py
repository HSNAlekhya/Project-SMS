from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # keep only a single dropdown for course selection (selected_course)
        fields = ['first_name', 'last_name', 'email', 'roll_no', 'age', 'gender', 'attendance', 'selected_course','grade']
        widgets = {
            'selected_course': forms.Select(),
            'gender': forms.Select(),
            'attendance': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'grade': forms.TextInput(attrs={'maxlength': 3}),
        }
        labels = {
            'selected_course': 'Course',
            'gender': 'Gender',
            'attendance': 'Attendance (%)',
            'grade': 'Grade',
        }
