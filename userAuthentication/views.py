from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitor.forms import BookARoom
from visitor.util import total_rooms
from visitor.models import Visitor, BookingInfo
from django.utils import timezone
from userAuthentication.forms import EditRequests
from django.http import HttpResponseRedirect


@login_required
def homepage(request):
    if request.user.is_staff:
        return HttpResponseRedirect(reverse('staff_homepage'))
    booking_info = BookingInfo.objects.filter(visitor__user=request.user).filter(visitor__is_departed=False)
    current_request = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    # mylist = zip(current_requests, booking_info)
    rooms = total_rooms()
    if request.method == "POST":
        form = BookARoom(request.POST)
        if current_request:
            return HttpResponseRedirect(reverse('homepage'))
        if form.is_valid():
            required_rooms = form.cleaned_data.get('no_of_rooms_required')
            Visitor.objects.create(user=request.user, no_of_rooms_required=required_rooms,
                                   date_of_booking=timezone.now())
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BookARoom()
        # for r, b in mylist:
        #     print(b.room_no, b.hostel_allotted)
    return render(request, 'homepage/home.html',
                  {'form': form, 'rooms': rooms, 'current_request': current_request,
                   'booking_info': booking_info})


@login_required()
def edit(request):
    try:
        visitor = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    except Visitor.DoesNotExist:
        return HttpResponseRedirect(reverse('homepage'))
    if visitor.status:
        HttpResponseRedirect(reverse('homepage'))
    current_request = Visitor.objects.filter(user=request.user).filter(is_departed=False).first()
    if current_request:
        if request.method == 'POST':
            form = EditRequests(request.POST)
            if form.is_valid():
                visitor.no_of_rooms_required = form.cleaned_data.get('no_of_rooms_required')
                visitor.from_date = form.cleaned_data.get('from_date')
                visitor.to_date = form.cleaned_data.get('to_date')
                visitor.room_preference = form.cleaned_data.get('room_preference')
                visitor.save(update_fields=['no_of_rooms_required', 'from_date', 'to_date', 'room_preference'])
                return HttpResponseRedirect(reverse('homepage'))
        else:
            initial_data = {
                'no_of_rooms_required': visitor.no_of_rooms_required,
                'from_date': visitor.from_date,
                'to_date': visitor.to_date,
                'room_preference': visitor.room_preference,
            }
            form = EditRequests(initial=initial_data)
        return render(request, 'homepage/edit.html', {'form': form})
