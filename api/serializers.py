from rest_framework  import serializers
from app.models import Study_center, Teacher, Student

class Study_centerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Study_center
        fields = '__all__'


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'        
