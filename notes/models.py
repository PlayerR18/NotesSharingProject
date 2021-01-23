from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=3)
    role = models.CharField(max_length=15)


def __str__(self):
    return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=3)
    subject = models.CharField(max_length=15)
    notesfiles = models.FileField(max_length=10, null=True)
    filetype = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=10)


def __str__(self):
    return self.signup.user.username + " " + self.status
