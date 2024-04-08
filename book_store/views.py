from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

from .forms import CreateUserForm
def index(request):

    return render(request, "index.html")

def logins(request):
    if request.method=='POST':
     username=request.POST.get('username')
     password=request.POST.get('password')
     
     user=authenticate(request,username=username,password=password)
     print(user)
     if user is not None:
        
        login(request,user)
       
        return HttpResponseRedirect('bookinsert')
    return render(request,"login.html")
def register(request):
    form =CreateUserForm()
   
    if request.method =='POST':
        
        form =CreateUserForm(request.POST)
        
        
        if form.is_valid():
        
          form.save()
          return HttpResponseRedirect("login")
          
    return render(request,"register.html",{'form':form})
def bookinsert(request):
   return render(request,"bookinsert.html")