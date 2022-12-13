from django.shortcuts import redirect, render
from .forms import userForm,updateUser
from .models import user_signup

# Create your views here.

def index(request):
    if request.method=='POST': #true
        user=userForm(request.POST)
        if user.is_valid(): #true
            user.save()
            print("Your account has been created!")
            return redirect('showdata')
        else: #false    
            print(user.errors)
    return render(request,'index.html')

def showdata(request):
    data=user_signup.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=user_signup.objects.get(id=id)
    if request.method=='POST':
        updateuser=updateUser(request.POST)
        if updateuser.is_valid():
            updateuser=updateUser(request.POST,instance=stid)
            updateuser.save()
            print("Your data has been updated!")
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'user':user_signup.objects.get(id=id)})

def deletedata(request,uid):
    stid=user_signup.objects.get(id=uid)
    user_signup.delete(stid)
    return redirect('showdata')

