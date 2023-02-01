from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    empid = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    Status = models.BooleanField(default=False)

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')
    status_description = models.TextField(null=False)

class upload(models.Model):
    Name = models.CharField(max_length=20)
    EmpID = models.CharField(max_length=20)
    Projectname = models.CharField(max_length=20)
    Document = models.FileField(upload_to='document')