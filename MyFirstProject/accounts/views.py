
from audioop import reverse
import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
from django.core.cache import cache
from django.contrib import  messages
from django.db.models import Q
from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect
# def cache_view(request):
#     mv=cache.get('movie','Nothing')
#     if mv=='Nothing':
#         cache.set('movie','Okay',30)
#         mv=cache.get('movie')
#     return render(request,'cache.html',{'mv':mv})

# def cache_view(request):
#     mv=cache.get_or_set('fees',3000,30)
#     return render(request,'cache.html',{'mv':mv})

# def cache_view(request):
#     data={'k1':'v1','k2':'v2','k3':'v3'}
#     cache.set_many(data,30)
#     cache.delete('k1')
#     mv=cache.get_many(data)
#     return render(request,'cache.html',{'mv':mv})

# def cache_view(request):
#     cache.set('roll',128)
#     mv=cache.get('roll')
#     return render(request,'cache.html',{'mv':mv})


# now the output for mv =128

# def cache_view(request):
#     cache.set('roll',128)
#     #cache.incr('key') will increase cache value by 1 (By default delta=1 sepecified) ,i.e 129 Here
#     mv=cache.incr('roll',delta=120)
#     return render(request,'cache.html',{'mv':mv})

# now the output for mv =248

# def cache_view(request):
#     cache.set('roll',128)
#     mv=cache.decr('roll',delta=120)
#     return render(request,'cache.html',{'mv':mv})
# def home(request):
#     if 'is_loggedin' in request.COOKIES and 'email' in request.COOKIES:
#         context={
#             'email':request.COOKIES['email'],
#             'status':request.COOKIES['is_loggedin']
#         }
#         return render(request,'home.html',context)
#     return render(request,'home.html')

# def cookie_login(request):
#     if request.method=='POST':
#         email=request.POST['email']
#         response=render(request,'home.html')
#         response.set_cookie('email',email)
#         response.set_cookie('is_loggedin','True')
#         print('Cookie set')
#         return render(request,'home.html')
#     return render(request,'cookie_login.html')
# def cookie_logout(request):
#     response=redirect('accounts/cookie_login')
#     response.delete_cookie('email')
#     response.delete_cookie('is_loggedin')
#     return redirect('home')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['pass']
        password2=request.POST['cpass']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Already Exists')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'REgistered Successfully')
                return redirect('login')
        else:
            messages.error(request,'Incorrect Password')
            return render(request,'register.html')

    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        if auth.authenticate(username=username,password=password):
            print('Authenticated')
            return redirect('/')
        else:
            messages.error(request,'INVALID_DETAILS')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
