from incubation.settings import STATIC_URL
from rest_framework import HTTP_HEADER_ENCODING, response
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,BookingSerializer
from api.models import BookingForm
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework import status

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookingViewset(viewsets.ViewSet):
    
    def list(self,request):
        queryset = BookingForm.objects.all()
        serializer_class = BookingSerializer(queryset,many=True)
        return Response(serializer_class.data)

    def create(self,request):
        serializer_class = BookingSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_201_CREATED)
