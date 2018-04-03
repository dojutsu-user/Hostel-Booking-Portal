from django.db import models
from django.conf import settings
from hostel.models import Hostel
from hostel.util import generate_choices_of_hostels
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth import get_user_model

User = get_user_model()


class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    no_of_rooms_required = models.IntegerField(default=1)
    date_of_booking = models.DateTimeField(null=True, blank=True)
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
    visitor = models.OneToOneField(Visitor, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.visitor.user.username

    def required_rooms(self):
        return self.visitor.rooms_required()


def create_booking_info_object(instance, created, *args, **kwargs):
    if created:
        temp = BookingInfo.objects.create(visitor=instance)
        temp.save()
        return temp


def update_available_rooms_increase(instance, created, *args, **kwargs):
    hostel = Hostel.objects.all()
    if instance.status:
        booking_info = BookingInfo.objects.filter(visitor=instance)
        for temp in booking_info:
            hostel_obj = temp.hostel_allotted
            x = hostel[int(hostel_obj) - 1]
            x.total_available_rooms -= 1
            x.total_booked_rooms += 1
            x.save()


def update_available_rooms_after_delete(sender, instance, using, *args, **kwargs):
    hostel = Hostel.objects.all()
    if instance.status:
        booking_info = BookingInfo.objects.filter(visitor=instance)
        for temp in booking_info:
            hostel_obj = temp.hostel_allotted
            x = hostel[int(hostel_obj) - 1]
            x.total_available_rooms += 1
            x.total_booked_rooms -= 1
            x.save()


post_save.connect(create_booking_info_object, sender=Visitor)
post_save.connect(update_available_rooms_increase, sender=Visitor)
pre_delete.connect(update_available_rooms_after_delete, sender=Visitor)
