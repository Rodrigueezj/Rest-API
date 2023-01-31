from rest_framework import serializers
from .models import Report

#translates info into a json

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report 
        fields = ('id', 'date', 'price', 'description' )
