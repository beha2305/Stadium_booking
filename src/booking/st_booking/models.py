from django.db import models
from ..user.models import User
from ..stadium.models import Stadium


class Booking(models.Model):
    status_choices = (
        (1, 'Active'),
        (2, 'Cancelled'),
        (3, 'Booked'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.SmallIntegerField(choices=status_choices, null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stadium
