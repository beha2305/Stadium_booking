from rest_framework import viewsets, permissions
from booking.st_booking.models import Booking
from .serializer import BookingSerializer
from booking.api.v1.permission import IsStadiumOwner, AdminPermission, IsUser, IsAdminOrStadiumOwner


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):

        if self.action == 'create':
            permission_classes = [IsUser]
        elif self.action == 'list':
            permission_classes = [IsAdminOrStadiumOwner]
        elif self.action == 'destroy':
            permission_classes = [IsStadiumOwner]

        return [i() for i in permission_classes]



