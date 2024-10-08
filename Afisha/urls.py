from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
]
