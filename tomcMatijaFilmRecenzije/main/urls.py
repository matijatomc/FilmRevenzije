from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('film/', views.FilmView.as_view())
]