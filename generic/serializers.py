from rest_framework import serializers
from .models import Student2

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student2
        fields=['id','name','roll','city']