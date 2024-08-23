from rest_framework import serializers
from .models import Director, Movie, Review, CustomUser


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters long.")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_review_text(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Review text must be at least 10 characters long.")
        return value


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.generate_confirmation_code()
        return user


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = CustomUser.objects.get(username=data['username'])
            if user.confirmation_code != data['code']:
                raise serializers.ValidationError("Invalid code")
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User does not exist")
        return data

    def save(self):
        user = CustomUser.objects.get(username=self.validated_data['username'])
        user.is_active = True
        user.confirmation_code = None
        user.save()
