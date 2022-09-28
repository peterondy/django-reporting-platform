from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def logout(request):
    auth.logout(request)
    return redirect('/')