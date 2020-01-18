from rest_framework import serializers
from . import models

# Serializer for Movie model
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = ('id', 'movie_name', 'cast', 'release_year', 'ratings','description')