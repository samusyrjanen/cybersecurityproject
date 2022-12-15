from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .database_reader import get_all_notes, get_user_notes, write_note
#from django.views.decorators.csrf import csrf_protect

def index(request):
    users = User.objects.all()
    logged_in_user = str(request.user)
    if logged_in_user == 'AnonymousUser':
        logged_in_user = None
    return render(request, 'login.html', {'users': users, 'logged_in_user': logged_in_user})

#@csrf_protect
def notes(request, username):#broken access control: users can see other users' notes using the address field
    logged_in_user = str(request.user)
    if logged_in_user == 'AnonymousUser':
        return redirect('/')
    
    if request.method == 'POST' and logged_in_user:
        new_note = request.POST['note']
        write_note(new_note, logged_in_user)

    #broken access control solution:
    '''
    if logged_in_user != username:
        return redirect('/')
    '''

    notes = get_user_notes(username)
    return render(request, 'notes.html', {'notes': notes, 'logged_in_user': logged_in_user})

#@csrf_protect
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('/')

#@csrf_protect
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_email = request.POST['email']
        user_password = request.POST['password']
        user = User.objects.create_user(username, email=user_email, password=user_password)
        user.save()
    return redirect('/')

def user_logout(request):
    if str(request.user) != 'AnonymousUser':
        logout(request)
    return redirect('/')
