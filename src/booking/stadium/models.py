from django.db import models


class Stadium(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    contact_number = models.CharField(max_length=13, null=True, blank=True)
    booking_price_per_hour = models.IntegerField()
    description = models.CharField(max_length=200, null=True, blank=True)
    lat = models.IntegerField()
    long = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StadiumImage(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True, blank=False)
    image = models.FileField(upload_to='images', null=True, blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.image
