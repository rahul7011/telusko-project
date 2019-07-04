from django.shortcuts import render,redirect                    #added redirect support
from django.contrib.auth.models import User,auth                 #added support for user and auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        check = auth.authenticate(username=username,password=password)

        if check is not None:
             auth.login(request,check)
             return redirect('/')
        else:
            messages.info(request,'Invalid credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')




def register(request):

    if request.method == 'POST':                    #if method is post then answer this
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'username already exists!')
            return redirect('register')       
        elif User.objects.filter(email=email).exists():          
            messages.info(request,'email already exists!')
            return redirect('register')           
        else:
            user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password,username=username)
            user.save();          #above firstname is from main database and after equal is our given name
        return redirect('login')
    else:
        return render(request,'register.html')