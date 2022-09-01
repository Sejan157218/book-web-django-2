# from multiprocessing import AuthenticationError
# from django.shortcuts import redirect, render
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login,logout
# # from .forms import CreateUserForm,CreateAuthenticationForm
# from django.contrib.auth import authenticate
# # Create your views here.


# def signupPage(request):
#     form=CreateUserForm()

#     if request.method=='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             return redirect('bookapp:home')
#     else:
#         form=CreateUserForm()
#     return render(request,'accounts/signup.html',{'form':form})



# def loginPage(request):
#     form=CreateAuthenticationForm()
#     if request.method=="POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         print(email,password)
#         user = authenticate(email=email, password=password)
#         print(user)
#         if user is not None:
#             print('ooo')
#             login(request,user)
#             if 'next' in request.POST:
#                  return redirect(request.POST.get('next'))
#             else:
#                 return redirect('bookapp:home')  
#     else:
#         form=CreateAuthenticationForm()
#     return render(request,'accounts/login.html',{'form':form})

# def logout_view(request):

#     if request.method=="POST":
#         logout(request)
#         return redirect('bookapp:home')

import profile
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from BookApp.models import Profile
from django.contrib import messages
import random




class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

# class RegisterView(generic.CreateView):
#     form_class = RegisterForm
#     template_name = 'accounts/signup.html'
#     success_url = reverse_lazy('accounts:my_view')

def signupPage(request):
    form=RegisterForm
    if request.method=='POST':
        form=RegisterForm(request.POST)
        phone = request.POST.get("phone")
        profile=Profile.objects.all()
        print(phone)
        print('profile',profile)
        if form.is_valid():
            user=form.save()
            profile=Profile.objects.create(user=user,phone=phone)
            profile.save()
            login(request,user)
            return redirect('bookapp:home')
    else:
        form=RegisterForm()
    return render(request,'accounts/signup.html',{'form':form})   


def OtpPhone(request):
    return render(request,'accounts/loginOtp.html')  

def sentOtp(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        user=Profile.objects.filter(phone=phone)
        if user:
            otp=str(random.randint(1000,9999))
            profile=Profile.objects.get(phone=phone)
            profile.otp=otp
            profile.save()
            return redirect('accounts:confirmOtp',pk=phone)
        else:
            messages.error(request,"Phone Number Does't exist")
    return redirect('accounts:otp-phone-number')

def confirmOtp(request,pk):
    return render(request,'accounts/confirmOtp.html',{'phone':pk}) 


def VerifyOtp(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        otp=int(request.POST.get('confirm-otp'))
        user=Profile.objects.get(phone=phone)
      
        if int(otp)==user.otp:
            print('phone',phone)
            login(request,user.user)
            if 'next' in request.POST:
                 return redirect(request.POST.get('next'))
            else:
                return redirect('bookapp:home')  
       
    messages.error(request,"OTP Does't Mach")
    return render(request,'accounts/confirmOtp.html',{'phone':phone})  


def logout_view(request):
     if request.method=="POST":
        logout(request)
        return redirect('bookapp:home')

    
