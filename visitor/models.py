from django.db import models
from django.conf import settings
from hostel.models import Hostel
from hostel.util import generate_choices_of_hostels
from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    no_of_rooms_required = models.IntegerField(default=1)
    from_date = models.DateField(default=timezone.now().date())
    to_date = models.DateField(default=timezone.now().date())
    date_of_booking = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='Confirm Booking')
    is_arrived = models.BooleanField(default=False, verbose_name="Arrived")
    arrived_at = models.DateTimeField(null=True, blank=True, )
    is_departed = models.BooleanField(default=False, verbose_name="Departed")
    departed_at = models.DateTimeField(null=True, blank=True)

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


def update_available_rooms_increase(sender, instance, *args, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if not obj.status == instance.status:
            if instance.status:
                hostel = Hostel.objects.all()
                booking_info = BookingInfo.objects.filter(visitor=obj)
                for temp in booking_info:
                    print(temp.hostel_allotted)


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


def update_is_arrived(sender, instance, *args, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if not obj.is_arrived == instance.is_arrived:
            if instance.is_arrived:
                instance.arrived_at = timezone.now()


def update_is_departed(sender, instance, *args, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if not obj.is_departed == instance.is_departed:
            if instance.is_departed:
                instance.departed_at = timezone.now()

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
pre_save.connect(update_is_arrived, sender=Visitor)
pre_save.connect(update_is_departed, sender=Visitor)
