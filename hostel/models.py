from django.db import models


class Hostel(models.Model):
    name = models.CharField(max_length=10)
    total_rooms = models.IntegerField()
    total_available_rooms = models.IntegerField()
    total_booked_rooms = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def available_rooms(self):
        return self.total_available_rooms