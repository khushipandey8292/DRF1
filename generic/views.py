from django.shortcuts import render
from .models import Student2
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student2.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student2.objects.all()
    serializer_class=s=StudentSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student2.objects.all()
    serializer_class=StudentSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=Student2.objects.all()
    serializer_class=StudentSerializer
    
    def patch(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student2.objects.all()
    serializer_class=StudentSerializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)