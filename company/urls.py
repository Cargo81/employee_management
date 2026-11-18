from django.urls import path
from . import views

urlpatterns = [
    #department
    path('departments/', views.department_list),
    path('departments/<int:pk>/', views.department_detail),
    
    #employee
    path('employee/', views.employee_list),
    path('employee/<int:pk>/', views.employee_detail),
]
