# movie_app/admin.py

from django.contrib import admin
from .models import Movie, Director, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')  # Убедитесь, что эти поля существуют в модели Movie

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'review_text')  # Убедитесь, что эти поля существуют в модели Review
