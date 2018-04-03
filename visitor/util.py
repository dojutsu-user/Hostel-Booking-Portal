from hostel.models import Hostel


def total_rooms():
    room = 0
    for h in Hostel.objects.all():
        room += h.available_rooms()
    return room
