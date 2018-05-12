from hostel.models import Hostel
from visitor.models import BookingInfo
from django.db.models import Q


def total_rooms():
    """
    return total number of available rooms for booking
    """
    try:
        room = 0
        for h in Hostel.objects.all():
            room += h.available_rooms()
        return room
    except:
        return 0


def list_of_hostels():
    """
    returns the list of hostels.
    """
    return ['VH1', 'VH2', 'VH3']


def get_zip_hostel_room(visitor):
    """
    returns the list of allotted room numbers with the corresponding hostel and the type of the room.
    """
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
