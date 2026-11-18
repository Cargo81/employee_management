from django.contrib import admin
from .models import (Department, Employee,
                     EmployeeProfile, Project)

# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_name')
    search_fields = ('department_name',)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'email', 'salary', 'department', 'is_active')
    list_filter = ('department', 'is_active')
    search_fields = ('employee_name', 'email')
    
@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('employee', 'phone')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'project_name',
        'start_date',
        'end_date',
        'is_completed'
    )

    list_filter = ('is_completed',)
    search_fields = ('project_name',)
    filter_horizontal = ('employees',)