from django.contrib import admin
from .models import Movie, Director, Review, Code

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'director')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'stars', 'review_text')

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'confirmation_code', 'created_at')
