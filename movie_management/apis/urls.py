from django.urls import path

from . import views

# Movie related urls
urlpatterns = [
    path('', views.MovieList.as_view()),
    path('<int:pk>/', views.MovieDetail.as_view()),
]