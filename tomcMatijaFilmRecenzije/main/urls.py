from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup_view),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main:login'), name='logout'),
    path('film/', views.FilmView.as_view()),
    path('film/<int:movie_id>/', views.movie_detail, name='film_detalji'),
    path('recenzija/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('recenzija/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('recenzije/', views.recenzije)
]