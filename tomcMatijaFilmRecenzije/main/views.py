from django.views.generic import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from .forms import RecenzijaForm

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
    
def movie_detail(request, movie_id):
    movie = get_object_or_404(Film, id=movie_id)
    recenzije = Recenzija.objects.filter(film_id=movie_id)

    # Handle form submission
    if request.method == 'POST':
        form = RecenzijaForm(request.POST)
        if form.is_valid():
            ocjena = form.cleaned_data['ocjena']
            recenzija_text = form.cleaned_data['recenzija']

            # Create a new review
            Recenzija.objects.create(
                autorRecenzije=request.user,
                ocjena=ocjena,
                recenzija=recenzija_text,
                film=movie
            )

            # Redirect to the same page to avoid form resubmission on refresh
            return redirect('main:film_detalji', movie_id=movie.id)
    else:
        form = RecenzijaForm()

    return render(request, 'film_detalji.html', {'movie': movie, 'recenzije': recenzije, 'form': form})


def edit_review(request, review_id):
    review = get_object_or_404(Recenzija, id=review_id)

    if request.method == 'POST':
        form = RecenzijaForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('main:film_detalji', movie_id=review.film.id)
    else:
        form = RecenzijaForm(instance=review)

    return render(request, 'edit_review.html', {'form': form, 'review': review})

def delete_review(request, review_id):
    review = get_object_or_404(Recenzija, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('main:film_detalji', movie_id=review.film.id)

    return redirect('main:film_detalji', movie_id=review.film.id)