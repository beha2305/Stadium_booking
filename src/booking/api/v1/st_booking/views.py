from rest_framework import viewsets, permissions
from booking.st_booking.models import Booking
from .serializer import BookingSerializer
from booking.api.v1.permission import AdminPermission


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    extra_kwargs = {
        "password": {
            "write_only": True
        }
    }

    # def get_permission(self):
    #     if self.action in ['retrieve', 'list']:
    #         permission_classes = [permissions.AllowAny]
    #     else:
    #         permission_classes = [AdminPermission]
    #     return [i() for i in permission_classes]
