from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cars
from rest_framework.response import Response
from .serializer import CarSerializer


# Create your views here.
class CarAPIView(APIView):
    
    # quaryset = Cars

    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarSerializer(cars , many = True)
        return Response(serializer.data)