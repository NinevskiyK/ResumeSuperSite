from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume_name = models.CharField(max_length=100)
    # about person
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # university
    university_name = models.CharField(max_length=100)
    university_specialization = models.CharField(max_length=100)
    university_start_date = models.DateField()
    university_end_date = models.DateField()
    # work
    work_name = models.CharField(max_length=100)
    work_specialization = models.CharField(max_length=100)
    work_start_date = models.DateField()
    work_end_date = models.DateField()
    work_projects = models.TextField()
    # about yourseld
    skills = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=100)




