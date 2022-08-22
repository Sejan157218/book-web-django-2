# from django import forms
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.contrib.auth.models import User


# class CreateUserForm(UserCreationForm):

#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )


# class CreateAuthenticationForm(AuthenticationForm):

#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     class Meta:
#         model = User
#         fields = ('email', 'password' )



from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')