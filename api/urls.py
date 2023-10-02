from django.urls import path, include
from .views import student, study_center, teacher, student_detail, study_center_detail, teacher_detail

urlpatterns = [
    path('student/', student),
    path('student/<int:pk>/', student_detail),
    path('teacher/', teacher),
    path('teacher/<int:pk>/', teacher_detail),
    path('study_center/', study_center),
    path('study_center/<int:pk>/', study_center_detail),
    path('auth/', include('dj_rest_auth.urls'))
    
    

]