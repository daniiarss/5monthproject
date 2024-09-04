from django.urls import path
from .views import (
    DirectorListView, DirectorDetailView, DirectorCreateView, DirectorUpdateView, DirectorDeleteView,
    MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView, MovieDeleteView,
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
    UserConfirmationView, RegisterUserView
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('confirm/', UserConfirmationView.as_view(), name='user-confirm'),
    path('directors/', DirectorListView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorDetailView.as_view(), name='director-detail'),
    path('directors/add/', DirectorCreateView.as_view(), name='director-create'),
    path('directors/<int:pk>/edit/', DirectorUpdateView.as_view(), name='director-update'),
    path('directors/<int:pk>/delete/', DirectorDeleteView.as_view(), name='director-delete'),

    path('movies/', MovieListView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/add/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie-delete'),

    path('reviews/', ReviewListView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('reviews/add/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review-update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),

    path('confirm/', UserConfirmationView.as_view(), name='user-confirm'),
]
