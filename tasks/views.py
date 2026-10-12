from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

from tasks.serializers import SignupSerializer
from tasks.serializers import TaskSerializer
from tasks.models import Task

# Create your views here.

class SignupView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=SignupSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            qs=User.objects.create_user(**cleaned_data)
            ser_inst=SignupSerializer(qs)
            return Response(data=ser_inst.data)
        else:
            return Response(data=serializer_instance.errors)

class TaskCreateListView(APIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request):
        user=request.user
        qs=Task.objects.filter(created_by=user)
        serializer_instance=TaskSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=TaskSerializer(data=form_data)
        if serializer_instance.is_valid():
                serializer_instance.save(created_by=request.user)
                return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TaskRetriveUpdateDeleteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,pk=None):
        instance=get_object_or_404(Task,id=pk)
        serializer_instance=TaskSerializer(instance)
        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):
        instance=get_object_or_404(Task,id=pk)
        self.check_object_permissions(request,instance)
        form_data=request.data
        serializer_instance=TaskSerializer(data=form_data,instance=instance)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        instance=get_object_or_404(Task,id=pk)
        self.check_object_permissions(request,instance)
        instance.delete()
        return Response({"message":"Data Deleted ..."})
