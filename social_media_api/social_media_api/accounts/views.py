from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer, LoginSerializer,
CustomUserSerializer

# Create your views here.
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': CustomUserSerializer(user).data, 'token': token.key}),


def login(request):
       serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validate_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'user': CustomUserSerializer(user).data, 'token': token.key}),


def profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
        elif request.method =='PUT':
            serializer = CustomUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_ok)