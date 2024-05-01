from django.db import models
from ..user.models import User

class Stadium(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    contact_number = models.CharField(max_length=13, null=True, blank=True)
    booking_price_per_hour = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class StadiumImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.stadium
