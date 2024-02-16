# sportFacilities/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SportsFacility
from .serializers import SportsFacilitySerializer

class SportsFacilityListAPIView(APIView):
    def get(self, request):
        facilities = SportsFacility.objects.all()
        serializer = SportsFacilitySerializer(facilities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SportsFacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
