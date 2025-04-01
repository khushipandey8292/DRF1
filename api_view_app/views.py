from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student1
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView

#function based api views

# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello world'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method=="POST":
#         return Response({'msg':'This is post request'})

# @api_view(['GET','POST'])
# def hello_world(request):
#     if request.method=="GET":
#         return Response({'msg':'This is GET request'})
#     if request.method=="POST":
#         return Response({'msg':'This is post request','data':request.data})




# @api_view(['GET','POST','PUT','PATCH','DELETE'])
# def hello_world(request,pk=None):
#     if request.method=='GET':
#         id=pk
#         # id=request.data.get('id')
#         if id is not None:
#             stu=Student1.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
        
#         stu=Student1.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data) 
    
#     if request.method=='POST':
#        serializer=StudentSerializer(data=request.data) 
#        if serializer.is_valid():
#            serializer.save()
#            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
       
#     if request.method=='PUT':
#         # id=request.data.get('id')
#         id=pk
#         stu=Student1.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"data updated"})
     
#     if request.method=='PATCH':
#         # id=request.data.get('id')
#         id=pk
#         stu=Student1.objects.get(pk=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':"data updated"})
           
#     if request.method=='DELETE':
#         id=request.data.get('id')
#         stu=Student1.objects.get(pk=id)
#         stu.delete()
#         return Response({"msg":"data deleted"})
    
    
# class based api view
class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student1.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        
        stu=Student1.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data) 
    
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data) 
        if serializer.is_valid():
           serializer.save()
           return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
       