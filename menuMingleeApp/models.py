from django.db import models
import datetime
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
class Restaurant(models.Model):
    restaurantId=models.IntegerField(null=True,blank=True)
    name=models.CharField(max_length=100,blank=True,null=True,default=None)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE,null=True)
    desc=models.CharField(max_length=300,blank=True,null=True,default=None)
    image=models.ImageField(upload_to='image/',blank=True,null=True)
    def __str__(self):
        return str(self.name)
class Type(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.name)
class Dish(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    subType=models.ForeignKey(Type,on_delete=models.CASCADE)
    dishId=models.IntegerField(null=True,default=0)
    name=models.CharField(max_length=40,blank=True,null=True)
    price=models.DecimalField(max_digits=8,decimal_places=2,null=True,default=0.0)
    image=models.ImageField(upload_to='image/' ,blank=True,null=True)
    desc=models.CharField(max_length=100,blank=True,null=True,default=None)
    def __str__(self):
        return str(self.name)+" - "+str(self.dishId)
class Vote(models.Model):
    vId=models.IntegerField(null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,null=True)
    winner=models.IntegerField(default=0,null=True,blank=True)
    def __str__(self):
        return str(self.date)