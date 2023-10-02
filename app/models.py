from django.db import models


class Study_center(models.Model):
    name = models.CharField('Name', max_length=256)
    def str(self):
        return f'{self.name}'    
    


class Teacher(models.Model):
    name = models.CharField('Name', max_length=256)
    about = models.TextField()
    experience = models.PositiveIntegerField()
    study_center = models.ForeignKey(Study_center, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)
    def str(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField('Name', max_length=256)    
    about = models.TextField()
    phone_number = models.CharField('Phone Number', max_length=256)
    study_center = models.ForeignKey(Study_center, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    def str(self):
        return f'{self.name}'