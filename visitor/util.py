from visitor.models import Visitor
from hostel.models import Hostel


def total_rooms():
    room = 0
    for h in Hostel.objects.all():
        room += h.available_rooms()
    return room


def no_of_rooms(request):
    try:
        visitor = Visitor.objects.get(user=request.user)
        return visitor.rooms_required()
    except Visitor.DoesNotExist:
        return 1
