from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_Aty = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Register_Number


class Feedback(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
