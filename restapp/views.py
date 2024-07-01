from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request,id=None):
    if request.method=='GET':
        if id==None:
            try:
                students=Student.objects.all()
                students_serialized=StudentSerializer(students,many=True)
                students_json=JSONRenderer().render(students_serialized.data)
                return HttpResponse(students_json,content_type='application/json',status=200)
            except Student.DoesNotExist:
                return HttpResponse('No Students Exist',status=400)
        else:
            try:
                student=Student.objects.get(id=id)
                student_serialized=StudentSerializer(student)
                student_json=JSONRenderer().render(student_serialized.data)
                return HttpResponse(student_json,content_type='application/json',status=200)
            except Student.DoesNotExist:
                return HttpResponse('Student with given id Does not exist',status=400)
    elif request.method=='POST':
        student_json=request.body
        student_stream=io.BytesIO(student_json)
        student_parsed=JSONParser().parse(student_stream)
        student_deserialized=StudentSerializer(data=student_parsed)
        if student_deserialized.is_valid():
            student_deserialized.save()
            return HttpResponse(student_json,content_type='application/json',status=201)
        return HttpResponse('Unable to create Student',status=400)
    elif request.method=='PUT':
        if id!=None:
            try:
                student_old=Student.objects.get(id=id)
                student_json=request.body
                student_stream=io.BytesIO(students_json)
                student_parsed=JSONParser().parse(student_stream)
                student_deserialized=StudentSerializer(student_old,data=student_parsed)
                if student_deserialized.is_valid():
                    student_deserialized.save()
                    return HttpResponse(student_json,content_type='application/json',status=200)
                return HttpResponse('Unable to Update Student',status=400)
            except Student.DoesNotExist:
                return HttpResponse('Student with given id does not exist',status=400)
        else:
            return HttpResponse('Student with out id cannot be updated',status=400)
    elif request.method=='DELETE':
        print(id)
        if id!=None:
            try:
                student=Student.objects.get(id=id)
                student.delete()
                return HttpResponse('Student Deleted',status=204)
            except Student.DoesNotExist:
                return HttpResponse('Student with Given id not found',status=400)
        else:
            return HttpResponse('Student with out id cannot be deleted',status=400)
    

