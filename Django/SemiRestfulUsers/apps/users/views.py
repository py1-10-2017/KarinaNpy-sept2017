from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "users/edit.html", context)

def show(request, user_id):
    context = {
        'user': User.objects.get(id = user_id)
    }
    return render(request, "users/show.html", context)

def create(request):
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
    )
    return redirect('/users')

def update(request, user_id):
    user_now = User.objects.get(id = user_id)
    user_now.first_name = request.POST['first_name']
    user_now.last_name = request.POST['last_name']
    user_now.email = request.POST['email']
    user_now.save()
    return redirect('/users')

def destroy(request, user_id):
    User.objects.get(id = user_id).delete()
    return redirect('/users')
