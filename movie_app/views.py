from rest_framework import viewsets
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Afisha project!")


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

