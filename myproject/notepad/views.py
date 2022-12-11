from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .database_reader import get_all_notes, get_user_notes, write_note

def index(request):
    users = User.objects.all()
    logged_in_user = str(request.user)
    if logged_in_user == 'AnonymousUser':
        logged_in_user = None
    return render(request, 'login.html', {'users': users, 'logged_in_user': logged_in_user})

def notes(request, username):
    logged_in_user = str(request.user)
    if logged_in_user == 'AnonymousUser':
        logged_in_user = None
    
    if request.method == 'POST' and logged_in_user:
        new_note = request.POST['note']
        write_note(new_note, logged_in_user)

    notes = get_user_notes(username)
    return render(request, 'notes.html', {'notes': notes, 'logged_in_user': logged_in_user})

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']
        user = User.objects.create_user(username, email=None, password=user_password)
        user.save()
    return redirect('/')

def user_logout(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
    return redirect('/')
