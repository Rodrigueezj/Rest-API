from django.shortcuts import render
from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer

class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all() #los objetos de la database
    serializer_class = ReportSerializer #cuál serializer se va a usar?