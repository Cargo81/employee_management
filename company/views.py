from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Department,Employee,EmployeeProfile,Project
from .serializers import DepartmentSerializer,EmployeeSerializer,EmployeeProfileSerializer,ProjectSerializer,UserRegistrationSerializer
from .permissions import IsAdminOrHR, IsAdmin, IsAdminHRReadOnly

@api_view(['GET', 'POST'])
@permission_classes([IsAdminHRReadOnly])
def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#department details API
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminHRReadOnly])
def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        department.delete()
        return Response(
            {'message':'Department deleted successfully'},
            status=status.HTTP_200_OK
        )
        
#employee CRUD API
@api_view(['GET', 'POST'])
@permission_classes([IsAdminHRReadOnly])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.select_related('department').all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#employee detail API:
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminHRReadOnly])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        employee.delete()
        return Response(
            {'message': 'Employee deleted successfully'},
            status=status.HTTP_200_OK
        )
        
#employee profile API (one-to-one)
@api_view(['GET', 'POST'])
@permission_classes([IsAdminHRReadOnly])
def employee_profile_list(request):
    if request.method == 'GET':
        profiles = EmployeeProfile.objects.select_related('employee').all()
        serializer = EmployeeProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeProfileSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Employee Profile Detail API
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminHRReadOnly])
def employee_profile_detail(request, pk):

    profile = get_object_or_404(
        EmployeeProfile,
        employee_id=pk
    )

    if request.method == 'GET':
        serializer = EmployeeProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeProfileSerializer(
            profile,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#project api(many-to-many)
@api_view(['GET', 'POST'])
@permission_classes([IsAdminHRReadOnly])
def project_list(request):
    
    if request.method == 'GET':
        projects = Project.objects.prefetch_related('employees').all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Project Detail API
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminHRReadOnly])
def project_detail(request, pk):

    project = get_object_or_404(Project, pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(
            project,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#user registration   
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):

    serializer = UserRegistrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
                'message': 'User registered successfully',
                'user': UserRegistrationSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response({
        'message': 'Authentication successful',
        'username': request.user.username,
        'user_id': request.user.id,
    })