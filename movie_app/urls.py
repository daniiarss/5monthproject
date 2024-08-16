from django.urls import path
from .views import (
    DirectorListCreateAPIView,
    DirectorRetrieveAPIView,
    MovieListCreateAPIView,
    MovieRetrieveAPIView,
    ReviewListCreateAPIView,
    ReviewRetrieveAPIView,
    MovieReviewsListAPIView,
)

urlpatterns = [
    path('directors/', DirectorListCreateAPIView.as_view(), name='director-list'),
    path('directors/<int:id>/', DirectorRetrieveAPIView.as_view(), name='director-detail'),
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list'),
    path('movies/<int:id>/', MovieRetrieveAPIView.as_view(), name='movie-detail'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('reviews/<int:id>/', ReviewRetrieveAPIView.as_view(), name='review-detail'),
    path('movies/reviews/', MovieReviewsListAPIView.as_view(), name='movie-reviews-list'),
]
