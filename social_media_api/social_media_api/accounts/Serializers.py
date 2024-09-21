from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ('id', 'bio', 'profile', 'followers', 'username')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'bio', 'profile', 'username')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = Customuser.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            return user 
        raise serializers.ValidationError("you've inserted the wrong username or password please try again one more time")
