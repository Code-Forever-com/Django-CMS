from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label="Kullanıcı Adı")
    password = forms.CharField(max_length=100,label="Şifre",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password) 
            if not user: 
                raise forms.ValidationError("Yanlış Kullanıcı Adı veya Şifre Girdiniz!")
        return super(LoginForm,self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100,label="Kullanıcı Adı")
    email = forms.EmailField(max_length=100,label="E-posta",widget=forms.EmailInput)
    password = forms.CharField(max_length=100,label="Şifre",widget=forms.PasswordInput)
    passwordVerify = forms.CharField(max_length=100,label="Şifre Doğrulama",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "passwordVerify"
        ]

    def clean(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("Email girmediniz!")
        return super(LoginForm,self).clean()

    def clean_passwordVerify(self):
        password = self.cleaned_data.get("password")
        passwordVerify = self.cleaned_data.get("passwordVerify")
        if passwordVerify and password and passwordVerify != password:
            raise forms.ValidationError("Şifreler birbiriyle uyuşmuyor!")
        return password