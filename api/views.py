from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response

from .permisions import StudyPermission, StudyDetailPermission, StudentPermission, StudentDetailPermission, TeacherPermission, TeacherDetailPermission
from app.models import Study_center, Teacher, Student
from .serializers import Study_centerSerializers, TeacherSerializers, StudentSerializers

@api_view(['GET', 'POST'])
@permission_classes([StudyPermission])
def study_center(request):
    if request.method == 'GET':
        study_centers = Study_center.objects.all()
        serializer = Study_centerSerializers(study_centers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = Study_centerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE' ])
@permission_classes([StudyDetailPermission])
def study_center_detail(request, pk):

    study_centers = Study_center.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = Study_centerSerializers(study_centers) 
        return Response(serializer.data, status=HTTP_202_ACCEPTED)   
    elif request.method == 'PUT':
        serializer = Study_centerSerializers(study_centers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        study_centers.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([StudentPermission])
def student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializers(student, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE' ])
@permission_classes([StudentDetailPermission])
def student_detail(request, pk):

    students = Student.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializers(students) 
        return Response(serializer.data, status=HTTP_202_ACCEPTED)   
    elif request.method == 'PUT':
        serializer = StudentSerializers(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([TeacherPermission])
def teacher(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializers(teachers, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TeacherSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE' ])
@permission_classes([TeacherDetailPermission])
def teacher_detail(request, pk):

    teachers = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializers(teachers) 
        return Response(serializer.data, status=HTTP_202_ACCEPTED)   
    elif request.method == 'PUT':
        serializer = TeacherSerializers(teachers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teachers.delete()
        return Response(status=HTTP_204_NO_CONTENT)
