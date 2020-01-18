# from django.shortcuts import render
from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer


# View for creating and listing of movie details
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# View for getting, updating and deleting the specific movie details by its ID
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer