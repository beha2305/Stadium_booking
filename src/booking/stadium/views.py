from rest_framework.views import APIView
from .models import Stadium

class StadiumView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get_object(self, user_id):
        try:
            stadiums = Stadium.objects.all()
        except Stadium.DoesNotExist:
            stadiums = None

        return stadiums

    def get(self, request, *args, **kwargs):
        stadiums = Stadium.objects.all()
