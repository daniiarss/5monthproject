from django.urls import path
from .views import (
    DirectorListCreateAPIView,
    DirectorRetrieveUpdateDestroyAPIView,
    MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorRetrieveUpdateDestroyAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
]
