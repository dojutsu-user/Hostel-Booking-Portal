from hostel.models import Hostel


def total_rooms_available():
    try:
        rooms = 0
        for hostel in Hostel.objects.all():
            rooms += hostel.available_rooms()
        return rooms
    except:
        return 0


def generate_choices_of_hostels():
    # temp = ()
    # i = 1
    # if Hostel.objects.all().exists():
    # for h in Hostel.objects.all():
    #     temp += ((str(i), h.name),)
    #     i += 1
    #     return temp
    # else:
    #     temp_ = (
    #     ('None','None'),
    #     )
    #     return temp_
    temp = (('1', 'VH1'),
            ('2', 'VH2'),
            ('3', 'VH3'),)
    return temp
    # VH1 = Hostel.objects.get_or_create(name='VH1', total_rooms=30, total_available_rooms=30, total_booked_rooms=0)
    # VH2 = Hostel.objects.get_or_create(name='VH2', total_rooms=30, total_available_rooms=30, total_booked_rooms=0)
    # VH3 = Hostel.objects.get_or_create(name='VH3', total_rooms=30, total_available_rooms=30, total_booked_rooms=0)
    # temp = ()
    # i = 1
    # if Hostel.objects.all().exists():
    #     for h in Hostel.objects.all():
    #         temp += ((str(i), h.name),)
    #         i += 1
    #         return temp