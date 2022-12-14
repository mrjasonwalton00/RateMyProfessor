from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def index(request):
    return render(request, 'base/home.html')




# Accounts models.py
