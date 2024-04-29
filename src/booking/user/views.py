from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import JWTAuthentication
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework import status
from .models import User, Role, Permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer


class UserListApiView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser, IsOwner]

    def get_object(self, user_id):
        try:
            users = User.objects.get(id=user_id)
        except User.DoesNotExist:
            users = None

        return users

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):
        user = self.get_object(user_id)
        if not user:
            return Response({"error": "User does not find"}, status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response({"message": "User succesfully deleted!"})
