from django.urls import path, include
from booking.api.v1.user import urls as user_urls
from booking.api.v1.stadium import urls as stadium_urls
from booking.api.v1.st_booking import urls as st_booking_urls

urlpatterns = [
    path('user/', include(user_urls)),
    path('stadium/', include(stadium_urls)),
    path('booking/', include(st_booking_urls))
]