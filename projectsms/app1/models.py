from django.db import models


class Student(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	roll_no = models.CharField(max_length=20, unique=True)
	age = models.PositiveIntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.roll_no})"

# Create your models here.
