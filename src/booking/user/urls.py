from django.urls import path
from .views import UserListApiView

urlpatterns = [
    path('', UserListApiView.as_view()),
    path('delete/<int:user_id>/', UserListApiView.as_view())
]