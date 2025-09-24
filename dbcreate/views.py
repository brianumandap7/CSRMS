from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genders, Roles, Responder_tbl, Classification_tbl, Severity_tbl, TLP_tbl, Ticket_tbl, Status_tbl, IR_tbl
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

class gdb(APIView): # dbcreate/gdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Genders.objects.values())
        return Response(output)

class rodb(APIView): # dbcreate/rodb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Roles.objects.values())
        return Response(output)

class respdb(APIView): # dbcreate/respdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Responder_tbl.objects.values())
        return Response(output)

class classdb(APIView): # dbcreate/classdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Classification_tbl.objects.values())
        return Response(output)

class sevdb(APIView): # dbcreate/sevdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Severity_tbl.objects.values())
        return Response(output)

class tlpdb(APIView): # dbcreate/tlpdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(TLP_tbl.objects.values())
        return Response(output)
    
class ticketdb(APIView): # dbcreate/ticketdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Ticket_tbl.objects.values())
        return Response(output)

class statdb(APIView): # dbcreate/statdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(Status_tbl.objects.values())
        return Response(output)

class iprdb(APIView): # dbcreate/iprdb
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        output = list(IR_tbl.objects.values())
        return Response(output)