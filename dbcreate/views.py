from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genders
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class gdb(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Genders.objects.values())
        return Response(output)


