from django.views.generic import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def home(request):
    return render(request,  'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            context = {"message":"Passwords do not match"}
            return render(request, 'signup.html', context)

        if User.objects.filter(username=username).exists():
            context = {"message":"Username already exists"}
            return render(request, 'signup.html', context)

        if User.objects.filter(email=email).exists():
            context = {"message":"Email already exists"}
            return render(request, 'signup.html', context)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/') 

    return render(request, 'signup.html')

def login_view(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = "Check your credentials. We didn't find a match!"

    context={'message':message}
    return render(request, 'login.html', context)

class FilmView(ListView):
    model = Film
    context_object_name = 'filmovi'
    template_name = 'film.html'

class RecenzijaView(ListView):
    model = Recenzija
    context_object_name = 'recenzije'
    template_name = 'recenzije.html'