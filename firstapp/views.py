import email
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import contactdata, contactform
from django.contrib.auth import authenticate, login
# Create your views here.
def website(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'firstapp/website.html')
    
def forgot(request):
      return render(request,'firstapp/forg_pswd.html')

def registration(request):
    if request.method=='POST':
      fname=request.POST.get('fname')
      sname=request.POST.get('sname')
      email=request.POST.get('email')
      mobile=request.POST.get('mobile')
      username=request.POST.get('username')
      password=request.POST.get('password')
      registration=contactdata(fname=fname,sname=sname, email=email, mobile=mobile, username=username, password=password)
      registration.save()
      messages.success(request, 'You are successfully registered!')
    return render(request,'firstapp/registration.html')
    
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        User = authenticate(username=username, password=password)

        if User is not None:
            # A backend authenticated the credentials
            login(request, User)
            messages.success(request, 'You are successfully signedin!')
            return redirect(registration)

        else:
            # No backend authenticated the credentials
            messages.success(request, 'Something is wrong!')
            return render(request,'firstapp/website.html')
    #messages.error(request, 'Something is wrong!')
    return render(request,'firstapp/login.html')
      
      
def contact(request):
      if request.method=='GET':
            return render(request,'firstapp/website/#contact.html')
    
      else:
        contactform(
            username=request.POST.get('username'),
            emailid=request.POST.get('emailid'),
            mobileno=request.POST.get('mobileno'),
        ).save()
        return render(request,'firstapp/website.html')

    
def condition(request):
      return render(request,'firstapp/conditions.html')
    
def privacy(request):
      return render(request,'firstapp/privacypolicy.html')