from django.shortcuts import render,redirect
from .forms import newuserForm
from .models import newUser
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=newUser.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login Sucessfully!")
            request.session['user']=unm #session create
            return redirect('home')
        else:
            print("Error! Username or Password does not match.")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=newuserForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect("/")
