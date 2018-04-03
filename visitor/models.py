from django.db import models
from django.conf import settings
from hostel.models import Hostel
from hostel.util import generate_choices_of_hostels
from django.db.models.signals import post_save


class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    no_of_rooms_required = models.IntegerField(default=1)
    date_of_booking = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Confirm Booking')

    def is_allotted(self):
        return self.status

    def rooms_required(self):
        return self.no_of_rooms_required

    def __str__(self):
        return self.user.username


class BookingInfo(models.Model):
    hostel_allotted = models.CharField(max_length=10, choices=generate_choices_of_hostels(), default="1")
    room_no = models.CharField(max_length=10, default='0000')
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    def __str__(self):
        return self.visitor.user.username

    def required_rooms(self):
        return self.visitor.rooms_required()


def create_booking_info_object(instance, created, *args, **kwargs):
    if created:
        temp = BookingInfo.objects.create(visitor=instance)
        temp.save()
        return temp


post_save.connect(create_booking_info_object, sender=Visitor)
