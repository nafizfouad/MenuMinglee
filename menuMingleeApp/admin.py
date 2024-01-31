from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Owner)
admin.site.register(Employee)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Type)