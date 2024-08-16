from django.contrib import admin
from django.urls import path, include
from movie_app.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('movie_app.urls')),
]
