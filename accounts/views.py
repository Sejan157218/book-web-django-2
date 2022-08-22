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

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout




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
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('bookapp:home')
    else:
        form=RegisterForm()
    return render(request,'accounts/signup.html',{'form':form})   




def logout_view(request):
     if request.method=="POST":
        logout(request)
        return redirect('bookapp:home')

    
