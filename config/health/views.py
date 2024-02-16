# health/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Health
from .serializers import HealthSerializer

class HealthListAPIView(APIView):
    def get(self, request):
        health_records = Health.objects.all()
        serializer = HealthSerializer(health_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
