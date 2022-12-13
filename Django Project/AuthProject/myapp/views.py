from django.shortcuts import render,redirect,HttpResponse
from .forms import newuserForm
from .models import newuser
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=newuser.objects.filter(username=unm,password=pas)
        if user: #true
            print("Login successfully!")
            request.session["user"]=unm #session create
            return redirect('home')
        else:
            #print("Error....Username or Password are wrong!")
            return HttpResponse("Error....Username or Password are wrong!")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        signupuser=newuserForm(request.POST)
        if signupuser.is_valid():
            signupuser.save()
            print("Signup Successfully!")
            return redirect('home')
        else:
            print(signupuser.errors)
    return render(request,'usersignup.html')

def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')
