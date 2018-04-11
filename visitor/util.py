from hostel.models import Hostel
from visitor.models import BookingInfo
from django.db.models import Q


def total_rooms():
    room = 0
    for h in Hostel.objects.all():
        room += h.available_rooms()
    return room


def list_of_hostels():
    l = []
    for h in BookingInfo.objects.all():
        l += [h.name]
    return l


def get_zip_hostel_room(visitor):
    booking_info = BookingInfo.objects.filter(
        ~Q(visitor=visitor),
        Q(visitor__status=True),
    )
    room = []
    hostel = []
    type_ = []
    for obj in booking_info:
        room += [obj.room_no]
        hostel += [obj.hostel_allotted]
        type_ += [obj.room_type]
    return room, hostel, type_
