from django.db import models

# Create your models here.

class MovieData(models.Model):
    # title = models.CharField(max_length=200)
    year = models.IntegerField()
    # genre = models.CharField(max_length=200)
    # director = models.CharField(max_length=200)
    # cast = models.CharField(max_length=200)
    # rating = models.IntegerField()
    # runtime = models.IntegerField()
    # plot = models.TextField()
    # poster = models.ImageField(upload_to='posters/')
    # trailer = models.URLField()
    # imdb_id = models.CharField(max_length=200)
    # imdb_rating = models.FloatField()
    # imdb_votes = models.IntegerField()
    # imdb_url = models.URLField()
    # imdb_genre = models.CharField(max_length=200)
    # imdb_runtime = models.IntegerField()
    # imdb_year = models.IntegerField()
    # imdb_poster = models.ImageField(upload_to='posters/')
    # imdb_trailer = models.URLField()
    imdb_plot = models.TextField()
    # imdb_director = models.CharField(max
    name = models.CharField(max_length=255)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=255, default='action')

    def __str__(self):
        return self.name