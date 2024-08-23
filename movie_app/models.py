from django.db import models
from django.contrib.auth import get_user_model
import random
import string

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    stars = models.PositiveIntegerField()

    def __str__(self):
        return f'Review for {self.movie.title}'

class Code(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = self.generate_confirmation_code()
        super().save(*args, **kwargs)

    def generate_confirmation_code(self):
        return ''.join(random.choices(string.digits, k=6))

    def __str__(self):
        return f'Code for {self.user.username}'
