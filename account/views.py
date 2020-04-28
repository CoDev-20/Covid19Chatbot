from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthForm, AccountUpdateForm
from django.http import HttpResponse, JsonResponse
import json

def registration_view(request):
    context = {'title': 'Signup'}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, email=email, password=raw_password)
            login(request,account)
            return render(request, 'chatbot_website/index.html', {'success':'success', 'title': 'Login'})
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'chatbot_website/pages/signup.html', context)

def logout_view(request):
    logout(request)
    return redirect('website-home')

def login_view(request):
    context = {'title': 'Login'}
    user = request.user

    if user.is_authenticated:
        return redirect('website-home')
    
    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('website-home')
    else:
        form = AccountAuthForm()
    
    context['login_form'] = form
    return render(request, 'chatbot_website/pages/login.html', context)

def account_update_view(request):
    context = {'title': 'Account'}

    if not request.user.is_authenticated:
        return redirect('website-login')

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                'email':request.user.email,
                'username':request.user.username,
                'firstName':request.user.firstName,
                'lastName':request.user.lastName,
            }
        )
    context['account_form'] = form
    return render(request, 'chatbot_website/pages/update.html', context)
    

def account(request):
    user = request.user

    if not request.user.is_authenticated:
        return redirect('website-login')
    else:
        return render(request, 'chatbot_website/pages/account.html', {'title': 'Account'})

# Create your views here.