from django.contrib import admin

from .models import Study_center, Teacher, Student

@admin.register(Study_center)
@admin.register(Teacher)
@admin.register(Student)


class Study_centerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')    

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') 
    list_display_links = ('id', 'name')   