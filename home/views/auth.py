from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def sign_up(request):
    params={}
    if request.method == 'POST' :
        email= request.POST.get('emailInput')
        password= request.POST.get('passwordInput')
        confirm_password= request.POST.get('confirmPasswordInput')

        if (len(User.objects.filter(username=email))==0) and (password==confirm_password):
            user = User.objects.create_user(username=email,email=email,password=password)
            user.save()
            params= {'message':'true','user_status':'true'}
            return redirect('sign_in')
        params= {'method':'true','user_status':'false','message':'user already exist'}
    return render(request,'home/signup.html',params)

def sign_in(request):  # sourcery skip: avoid-builtin-shadow
    params = {}
    if request.method == 'POST':
        email= request.POST.get('emailInput')
        password= request.POST.get('passwordInput')
        
        user = authenticate(request,username=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            next =  request.GET.get('next')
            print(next)
            if next is not None:
                return redirect(next)
        
    return render(request,'home/signin.html',params)

def sign_out(reqeust):
    logout(reqeust)
    return redirect('sign_in')