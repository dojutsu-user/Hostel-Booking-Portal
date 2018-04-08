from django import forms
from visitor.models import Visitor
from visitor.util import total_rooms
from django.utils import timezone
from .util import get_zip_hostel_room
import itertools


class BookARoom(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['no_of_rooms_required', 'from_date', 'to_date', 'room_preference']
        widgets = {
            'from_date': forms.DateInput(attrs=({
                'class': 'form-control',
                'id': 'datepicker',
            })),
            'to_date': forms.DateInput(attrs=({
                'class': 'form-control',
                'id': 'datepicker1',
            })),
            'no_of_rooms_required': forms.NumberInput(attrs=({
                'class': 'form-control'
            })),
            'room_preference': forms.Select(attrs=({
                'class': 'form-control'
            })),
        }

    def clean_no_of_rooms_required(self):
        rooms = total_rooms()
        required_rooms = self.cleaned_data.get('no_of_rooms_required')
        if required_rooms > rooms:
            raise forms.ValidationError("Required Rooms Are Not Available")
        elif required_rooms <= 0:
            raise forms.ValidationError("Please Enter Correct Value")
        return required_rooms

    def clean(self):
        from_ = self.cleaned_data.get('from_date')
        to_ = self.cleaned_data.get('to_date')
        present = timezone.now().date()
        if from_ > to_:
            raise forms.ValidationError("Please Enter Correct Dates")
        elif from_ < present:
            raise forms.ValidationError("Please Enter Correct Dates")
        return self.cleaned_data


class BookingInfoInlineAdminForm(forms.ModelForm):
    def clean(self):
        room, hostel, type = get_zip_hostel_room(self.cleaned_data.get('visitor'))
        room_get = self.cleaned_data.get('room_no')
        hostel_get = self.cleaned_data.get('hostel_allotted')
        type_get = self.cleaned_data.get('room_type0')
        # for h, r in l:
        #     if str(h) == str(hostel) and str(r) == str(room):
        #         raise forms.ValidationError("Room Already Allotted")
        for r, h, t in itertools.zip_longest(room, hostel, type):
            if str(r) == str(room_get) and str(h) == str(hostel_get) and str(t) == str(type_get):
                raise forms.ValidationError("Room Already Allotted")
        return self.cleaned_data


class VisitorAdminForm(forms.ModelForm):
    def clean(self):
        # is_arrived = self.cleaned_data.get('is_arrived')
        status = self.cleaned_data.get('status')
        is_departed = self.cleaned_data.get('is_departed')
        # if is_arrived and status is False:
        #     raise forms.ValidationError("Booking Is Not Confirmed Yet")
        # elif is_departed and status is False:
        #     raise forms.ValidationError("Booking Is Not Confirmed Yet")
        # elif is_departed and is_arrived is False:
        #     raise forms.ValidationError("Visitor Hasn't Arrived Yet")
        # return self.cleaned_data
        if not status and is_departed:
            raise forms.ValidationError("Booking Not Confirmed Yet")
        return self.cleaned_data
