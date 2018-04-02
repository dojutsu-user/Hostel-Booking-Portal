from django.db import models
from django.conf import settings
from hostel.models import Hostel
from hostel.util import generate_choices_of_hostels


class Visitor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    no_of_rooms_required = models.IntegerField(default=0)
    date_of_booking = models.DateTimeField(auto_now=True)
    hostel_allotted = models.CharField(default=1, choices=generate_choices_of_hostels(), max_length=10)
    rooms_allotted = models.CharField(max_length=10, default='0000')
    status = models.BooleanField(default=False, verbose_name='Confirm Booking')

    def is_allotted(self):
        return self.status

@receiver(post_save, sender=Visitor)
def update_no_of_rooms(sender, instance, **kwargs):
    if instance.is_allotted:
