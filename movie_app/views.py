from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Director, Movie, Review, Code
from django.contrib.auth import get_user_model
from django.http import HttpResponse
User = get_user_model()


def home(request):
    return HttpResponse("Welcome to the Afisha home page!")
class RegisterUserView(View):
    def post(self, request, *args, **kwargs):
        # Логика регистрации пользователя
        return JsonResponse({"message": "User registered successfully"})

class DirectorListView(ListView):
    model = Director
    template_name = 'director_list.html'

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'director_detail.html'

class DirectorCreateView(CreateView):
    model = Director
    fields = ['name']
    template_name = 'director_form.html'
    success_url = reverse_lazy('director-list-create')

class DirectorUpdateView(UpdateView):
    model = Director
    fields = ['name']
    template_name = 'director_form.html'
    success_url = reverse_lazy('director-list-create')

class DirectorDeleteView(DeleteView):
    model = Director
    template_name = 'director_confirm_delete.html'
    success_url = reverse_lazy('director-list-create')

class MovieListView(ListView):
    model = Movie
    template_name = 'movie_list.html'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'duration', 'director']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie-list-create')

class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'duration', 'director']
    template_name = 'movie_form.html'
    success_url = reverse_lazy('movie-list-create')

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list-create')

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    fields = ['movie', 'review_text', 'stars']
    template_name = 'review_form.html'
    success_url = reverse_lazy('review-list-create')

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['movie', 'review_text', 'stars']
    template_name = 'review_form.html'
    success_url = reverse_lazy('review-list-create')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('review-list-create')

class UserConfirmationView(View):
    def post(self, request, *args, **kwargs):
        code = request.POST.get('code')
        try:
            code_obj = Code.objects.get(code=code)
            user = code_obj.user
            user.is_active = True
            user.save()
            code_obj.delete()
            return redirect('success_page')
        except Code.DoesNotExist:
            return render(request, 'error_page.html', {'message': 'Invalid code'})
