from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
import random
import string
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

User = get_user_model()

def home(request):
    return HttpResponse("Welcome to the Afisha API!")


class ConfirmUserView(View):
    def post(self, request):
        code = request.POST.get('confirmation_code')
        if not code:
            return JsonResponse({'error': 'Confirmation code is required.'}, status=400)

        User = get_user_model()
        try:
            user = User.objects.get(confirmation_code=code)
            user.is_active = True
            user.confirmation_code = ''
            user.save()
            return JsonResponse({'message': 'User confirmed successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid confirmation code.'}, status=400)


class UserRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if not (username and password and email):
            return Response({'error': 'Username, password, and email are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        confirmation_code = ''.join(random.choices(string.digits, k=6))
        user.confirmation_code = confirmation_code
        user.save()

        send_mail(
            'Confirm your registration',
            f'Your confirmation code is {confirmation_code}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        return Response({'message': 'User registered. Please check your email to confirm your registration.'}, status=status.HTTP_201_CREATED)

class UserConfirmationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        confirmation_code = request.data.get('confirmation_code')
        try:
            user = User.objects.get(username=username, confirmation_code=confirmation_code)
            user.is_active = True
            user.confirmation_code = ''
            user.save()
            return Response({'message': 'User confirmed successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid confirmation code or username.'}, status=status.HTTP_400_BAD_REQUEST)
class DirectorListCreateAPIView(APIView):
    def get(self, request):
        return Response({'message': 'GET request for Directors'})

    def post(self, request):
        return Response({'message': 'POST request for Directors'})

class DirectorRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        return Response({'message': f'GET request for Director {pk}'})

    def put(self, request, pk):
        return Response({'message': f'PUT request for Director {pk}'})

    def delete(self, request, pk):
        return Response({'message': f'DELETE request for Director {pk}'})

class MovieListCreateAPIView(APIView):
    def get(self, request):
        return Response({'message': 'GET request for Movies'})

    def post(self, request):
        return Response({'message': 'POST request for Movies'})

class MovieRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        return Response({'message': f'GET request for Movie {pk}'})

    def put(self, request, pk):
        return Response({'message': f'PUT request for Movie {pk}'})

    def delete(self, request, pk):
        return Response({'message': f'DELETE request for Movie {pk}'})

class ReviewListCreateAPIView(APIView):
    def get(self, request):
        return Response({'message': 'GET request for Reviews'})

    def post(self, request):
        return Response({'message': 'POST request for Reviews'})

class ReviewRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        return Response({'message': f'GET request for Review {pk}'})

    def put(self, request, pk):
        return Response({'message': f'PUT request for Review {pk}'})

    def delete(self, request, pk):
        return Response({'message': f'DELETE request for Review {pk}'})
