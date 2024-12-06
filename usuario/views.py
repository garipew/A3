from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserLoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

# Create your views here.


class LoginView(APIView):
	permission_classes = [AllowAny]
	def post(self, request):
		serializer = UserLoginSerializer(data=request.data)
		if serializer.is_valid():
			username = serializer.validated_data['username']
			password = serializer.validated_data['password']
			user = authenticate(username=username, password=password)
			if user:
				token, created = Token.objects.get_or_create(user=user)
				return Response({'token': token.key})
			return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
