
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer,UserLoginSerializer
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterUser(APIView):
    def post(self,request,format=None):
        serializer=UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'msg':'User Created','token':token},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)
    

class LoginUser(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.data.get('username')
            password=serializer.data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'msg':'Login Success!','token':token},status=status.HTTP_200_OK)
            return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)