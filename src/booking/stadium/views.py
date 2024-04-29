from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import JWTAuthentication
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status
from .models import Stadium, StadiumImage
from .serializers import StadiumSerializer, StadiumImageSerializer


class StadiumView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, user_id):
        try:
            stadiums = Stadium.objects.all()
        except Stadium.DoesNotExist:
            stadiums = None

        return stadiums

    def get(self, request, *args, **kwargs):
        stadiums = Stadium.objects.all()
        
