from django.urls import path
from . import views

urlpatterns = [
    #department
    path('departments/', views.department_list),
    path('departments/<int:pk>/', views.department_detail),
    
    #employee
    path('employee/', views.employee_list),
    path('employee/<int:pk>/', views.employee_detail),
    
    #employee profile
    path('profiles/', views.employee_profile_list),
    path(
    'profiles/<int:pk>/',
    views.employee_profile_detail,
    name='profile-detail'
),
    
    #project
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail, name='project-detail'),
    
    path('register/', views.register_user, name='register_user'),
    
    path('test-auth/', views.test_auth, name='test-auth'),
]
