from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitor.forms import BookARoom
from visitor.util import total_rooms
from visitor.models import Visitor, BookingInfo
from django.utils import timezone


@login_required
def homepage(request):
    booking_info = BookingInfo.objects.filter(visitor__user=request.user).order_by('-visitor__date_of_booking')
    rooms = total_rooms()
    msg = ''
    current_requests = Visitor.objects.filter(user=request.user).order_by('-date_of_booking')
    mylist = zip(current_requests, booking_info)
    if request.method == "POST":
        form = BookARoom(request.POST)
        if form.is_valid():
            required_rooms = form.cleaned_data.get('no_of_rooms_required')
            Visitor.objects.create(user=request.user, no_of_rooms_required=required_rooms,
                                   date_of_booking=timezone.now())
            msg = "Request Submitted Successfully"
    else:
        form = BookARoom()
        for r,b in mylist:
            print(b.room_no, b.hostel_allotted)
    return render(request, 'homepage/home.html',
                  {'form': form, 'rooms': rooms, 'msg': msg, 'current_requests': current_requests,
                   'booking_info': booking_info, 'mylist': mylist})
