from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('HR', 'HR'),
        ('EMPLOYEE', 'Employee'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
class Department(models.Model):
    department_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.department_name
    
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.employee_name

class EmployeeProfile(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='employeesProfile', primary_key=True)
    phone = models.CharField(max_length=50)
    address = models.TextField(default=True)
    profile_image = models.ImageField(upload_to='employees/', blank=True, null=True)
    
    def __str__(self):
        return self.employee.employee_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name='projects', blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, default=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.project_name