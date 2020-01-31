from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

def firstapi(request):
    return HttpResponse("Hi")

def fetchDetails(request, id):
    return HttpResponse("Student Id : %s" % id)

class StudentView(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"studentList" : serializer.data})

    def post(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_obj = serializer.save()
        return Response("New Student Record created!")
        
