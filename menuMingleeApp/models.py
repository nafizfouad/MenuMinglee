from django.db import models

class Owner(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=30,blank=True)
    username=models.CharField(max_length=40,null=True,blank=True)
    password=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return str(self.name)
class Employee(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField(max_length=30,blank=True)
    username=models.CharField(max_length=40,null=True,blank=True)
    password=models.CharField(max_length=15,blank=True)
    def __str__(self):
        return str(self.name)