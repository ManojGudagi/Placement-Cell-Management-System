from django.db import models

# Create your models here.

class StudentModel(models.Model):
    student_name = models.CharField(max_length=250)
    student_email = models.EmailField(max_length=120)
    student_number = models.IntegerField(default=0)
    student_usn = models.CharField(max_length=10)
    student_branch = models.CharField(max_length=120)
    student_cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    student_resume = models.FileField(upload_to="resumes/", blank=True,null=True)



