# sportCategories/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SportCategory
from .serializers import SportCategorySerializer

class SportCategoryListAPIView(APIView):
    def get(self, request):
        categories = SportCategory.objects.all()
        serializer = SportCategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SportCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
