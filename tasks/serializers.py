from django.contrib.auth.models import User

from rest_framework import serializers

from tasks.models import Task


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
        read_only_fields=["id"]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=["created_at","updated_at"]