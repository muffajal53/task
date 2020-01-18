from django.db import models

# Model for Movie related Stuff
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    cast = models.TextField()
    description = models.TextField()
    release_year = models.IntegerField()
    ratings = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name