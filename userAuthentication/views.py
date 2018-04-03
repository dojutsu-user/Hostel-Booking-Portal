from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from visitor.forms import BookARoom
from visitor.util import total_rooms
from visitor.models import Visitor


@login_required
def homepage(request):
    rooms = total_rooms()
    msg = ''
    if request.method == "POST":
        form = BookARoom(request.POST)
        if form.is_valid():
            required_rooms = form.cleaned_data.get('no_of_rooms_required')
            visitor = Visitor.objects.create(user=request.user, no_of_rooms_required=required_rooms)
            visitor.save()
            msg = "Request Submitted Successfully"
    else:
        form = BookARoom()
    return render(request, 'homepage/home.html', {'form': form, 'rooms': rooms, 'msg': msg})
