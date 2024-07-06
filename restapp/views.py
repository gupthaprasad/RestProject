from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import Student
from .serializers import StudentSerializer


class StudentAPI(GenericAPIView,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    lookup_field='id'
    lookup_url_kwarg='id'

    def get(self,request,*args,**kwargs):
        if kwargs.get(self.lookup_url_kwarg) is not None:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
        
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    # def patch(self,request,*args,**kwargs):
    #     print('patch')
    #     return self.partial_update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)