from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = StudentModel


admin.site.register(StudentModel, StudentAdmin)