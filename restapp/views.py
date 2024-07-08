from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status


class StudentViewSet(viewsets.ViewSet):
    
    def list(self,request,*args,**kwargs):
        students=Student.objects.all()
        students_serialized=StudentSerializer(students,many=True)
        if students.exists():
            return Response(students_serialized.data,status=status.HTTP_200_OK)
        else:
            return Response([],status=status.HTTP_204_NO_CONTENT)
        
    def create(self,request,*args,**kwargs):
        student_deserialized=StudentSerializer(data=request.data)
        if student_deserialized.is_valid():
            student_deserialized.save()
            return Response(request.data,status=status.HTTP_201_CREATED)
        return Response(student_deserialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs['pk']
        try:
            student=Student.objects.get(id=id)
            student_serialized=StudentSerializer(student)
            return Response(student_serialized.data,status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response("Student with Give id Doesnot exist",status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Bad Request',status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,*args,**kwargs):
        id=kwargs['pk']
        if(id is not None):
            try:
                student=Student.objects.get(id=id)
                student_deserialized=StudentSerializer(student,data=request.data)
                if(student_deserialized.is_valid()):
                    student_deserialized.save()
                    return Response(student_deserialized.data,status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response("Student with Give id Doesnot exist",status=status.HTTP_204_NO_CONTENT)
            except:
                return Response('Bad Request',status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Student id required to update',status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,*args,**kwargs):
        id=kwargs['pk']
        if id is not None:
            try:
                student=Student.objects.get(id=id)
                student.delete()
                return Response('Deleted',status=status.HTTP_204_NO_CONTENT)
            except Student.DoesNotExist:
                return Response('Student with given id does not exist',status=status.HTTP_404_NOT_FOUND)
        else:
            return Response('Student id required to delete',status=status.HTTP_400_BAD_REQUEST)
            

        
    