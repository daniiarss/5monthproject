from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Afisha project!")

class DirectorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class MovieReviewsListAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

def get_queryset(self):
    return Movie.objects.all().prefetch_related('review_set')

