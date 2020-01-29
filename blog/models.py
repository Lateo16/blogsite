from django.db import models
import re


class Person(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    profile_img = models.FileField(blank=True, upload_to='images/')
        


class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=700)
    date = models.DateField()
    blogger = models.ForeignKey(Person, on_delete = models.CASCADE)

