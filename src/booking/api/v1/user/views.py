from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, RoleSerializer, PermissionSerializer, RolePermissionSerializer
from booking.user.models import User, Role, Permission
from booking.api.v1.permission import AdminPermission, IsStadiumOwner


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [AdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminPermission]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RolePermissionView(APIView):
    permission_classes = [AdminPermission]

    def patch(self, request, pk, *args, **kwargs):
        role = Role.objects.get(id=pk)
        serializer = RolePermissionSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            role.permission.set(serializer.validated_data['permission'])
            return Response(RoleSerializer(role).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)