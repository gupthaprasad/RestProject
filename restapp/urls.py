from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.student_api,name='student'),
    path('student/<int:id>/',views.student_api,name='student'),
]