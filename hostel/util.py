from hostel.models import Hostel


def total_rooms_available():
    rooms = 0
    for hostel in Hostel.objects.all():
        rooms += hostel.available_rooms()
    return rooms


def generate_choices_of_hostels():
    temp = ()
    i = 1
    for h in Hostel.objects.all():
        temp += ((i, h.name),)
        i += 1
    return temp