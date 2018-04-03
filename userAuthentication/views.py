from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitor.forms import BookARoom
from visitor.util import total_rooms
from visitor.models import Visitor
from django.utils import timezone


@login_required
def homepage(request):
    rooms = total_rooms()
    msg = ''
    current_requests = Visitor.objects.filter(user=request.user).order_by('-date_of_booking')
    if request.method == "POST":
        form = BookARoom(request.POST)
        if form.is_valid():
            required_rooms = form.cleaned_data.get('no_of_rooms_required')
            Visitor.objects.create(user=request.user, no_of_rooms_required=required_rooms,
                                   date_of_booking=timezone.now())
            msg = "Request Submitted Successfully"
    else:
        form = BookARoom()
    return render(request, 'homepage/home.html',
                  {'form': form, 'rooms': rooms, 'msg': msg, 'current_requests': current_requests})
