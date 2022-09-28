from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(signup)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(signup)
            else:
                user = User.objects.create_user(username=username, password=password, 
                                        email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                return redirect('http://127.0.0.1:8000/login/')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(signup)
            

    else:
        return render(request, 'signup/signup.html')