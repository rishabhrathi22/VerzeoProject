from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    Sid = serializers.IntegerField()
    FirstName = serializers.CharField(max_length=100)
    LastName = serializers.CharField(max_length=100)

    def create(self, data):
        return Student.objects.create(**data)
