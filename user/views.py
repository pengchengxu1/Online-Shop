import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from user.models import User


# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


class UserInfoForm(forms.Form):
    username = forms.CharField(label='username', max_length=50)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    phone = forms.CharField(label='phone', max_length=50)
    email = forms.CharField(label='email', max_length=50)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if not re_password or not password or not username or not email or not phone:
            messages.add_message(request, messages.ERROR, "args error!")
            return render(request, 'register.html')

        if password != re_password:
            messages.add_message(request, messages.ERROR, "password error!")
            return render(request, 'register.html')
        if "+86" in phone:
            phone = phone.replace("+86", "")
        if "@" not in email or "." not in email:
            messages.add_message(request, messages.ERROR, "email error!")
            return render(request, 'register.html')
        user = User.objects.filter(user_name__exact=username)
        if user:
            messages.add_message(request, messages.ERROR, "User name already exists!")
            return render(request, 'register.html')

        user = User()
        user.email = email
        user.phone = phone
        user.user_name = username
        user.pass_word = password
        user.save()

        return render(request, 'login.html')
    else:
        return render(request, 'register.html')


def logout(request):
    if request.method == 'GET':
        if request.session.get('username'):
            del request.session['username']
        return redirect('/index')


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(
                user_name__exact=username, pass_word__exact=password).first()

            if user:
                request.session["username"] = username
                userinfo = {
                    "islogin": 1,
                    "username": username
                }
                return redirect('/index', {"userinfo": userinfo})
            else:
                messages.add_message(request, messages.ERROR, "User name/password error!")
                return render(request, 'login.html')
        else:
            messages.add_message(request, messages.ERROR, "User name/password error!")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
