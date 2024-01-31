import re
import json
import datetime
from decimal import Decimal
from urllib import response
from io import BytesIO
from django.utils.html import strip_tags
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.template.loader import get_template,render_to_string
from django.views import View
from xhtml2pdf import pisa
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.db import IntegrityError
from django.contrib import messages
import json
import random
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group,User
from .models import *
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
def logIn(request):
    if 'login' in request.POST:
        if request.POST['type']=='1':
            owner=Owner.objects.filter(email=request.POST.get('email'))
            if not owner or owner[0].username is None:
                messages.error(request,'Account Does Not Exist',extra_tags='painai' )
            else:
                loginOwner=Owner.objects.get(email=request.POST.get('email'))
                if loginOwner.password==request.POST.get('pass'):
                    login(request,authenticate(request,username=loginOwner.username,email=loginOwner.email,password=loginOwner.password))
                    return redirect('/')
                else:
                    messages.error(request,'Passwords do not match !',extra_tags='painai')
        if request.POST['type']=='2':
            employee=Employee.objects.filter(email=request.POST.get('email'))
            if not employee or employee[0].username is None:
                messages.error(request,'Account Does Not Exist',extra_tags='painai' )
            else:
                loginEmployee=Employee.objects.get(email=request.POST.get('email'))
                if loginEmployee.password==request.POST.get('pass'):
                    login(request,authenticate(request,username=loginEmployee.username,email=loginEmployee.email,password=loginEmployee.password))
                    return redirect('/')
                else:
                    messages.error(request,'Passwords do not match !',extra_tags='painai')

    return render(request,'login.html')
def signUp(request):
    if 'signup' in request.POST:
        if request.POST['type']=='1':
            owner=Owner.objects.filter(email=request.POST.get('email'))
            if not owner:
                messages.error(request,'Enter a valid email',extra_tags='notFound')
            else:
                signUpOwner=Owner.objects.get(email=request.POST.get('email'))
                if signUpOwner.username is not None :
                    messages.error(request,'Account Already Exists!',extra_tags='painai')
                else:
                 signUpOwner.username=request.POST.get('user')
                 signUpOwner.password=request.POST.get('pass')
                 signUpOwner.save()
                 user=User.objects.create_user(username=request.POST.get('user'),email=request.POST.get('email'),password=request.POST.get('pass'))
                 messages.success(request,'Account Created Successfully!',extra_tags='ok')
        if request.POST['type']=='2':
            employee=Employee.objects.filter(email=request.POST.get('email'))
            if not employee:
                messages.error(request,'Enter a valid email',extra_tags='notFound')
            else:
                signUpEmployee=Employee.objects.get(email=request.POST.get('email'))
                if signUpEmployee.username is not None :
                    messages.error(request,'Account Already Exists!',extra_tags='painai')
                else:
                 signUpEmployee.username=request.POST.get("user")
                 signUpEmployee.password=request.POST.get('pass')
                 signUpEmployee.save()
                 user=User.objects.create_user(username=request.POST.get('user'),email=request.POST.get('email'),password=request.POST.get('pass'))
                 messages.success(request,'Account Created Successfully!',extra_tags='ok')
    return render(request,'signup.html')
def logOut(request):
    logout(request)
    return redirect('/logIn')