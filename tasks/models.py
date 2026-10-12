from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200,null=True)
    PRIORITY_CHOISES=(
        ("low",("low")),
        ("medium","medium"),
        ("high","high")
    )
    priority=models.CharField(max_length=100,
                              choices=PRIORITY_CHOISES,
                              default="low")
    category=models.CharField(max_length=200)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
