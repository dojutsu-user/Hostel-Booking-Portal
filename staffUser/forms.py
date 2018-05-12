from django import forms
from visitor.models import Visitor, BookingInfo
from django.contrib.auth import get_user_model
from django.forms.models import BaseInlineFormSet
from visitor.util import get_zip_hostel_room
from django.core.exceptions import ValidationError
import itertools


User = get_user_model()


class BooingAdminPanelForm(forms.ModelForm):
    """
    Form for staff users.
    """
    class Meta:
        model = BookingInfo
        fields = ['hostel_allotted', 'room_no', 'room_type']
        widgets = {
            'hostel_allotted': forms.Select(attrs=({
                'class': 'form-control',
            })),
            'room_no': forms.TextInput(attrs=({
                'class': 'form-control',
            })),
            'room_type': forms.Select(attrs=({
                'class': 'form-control',
            })),
        }


class booking_admin_panel_inline_form_base_form_set(BaseInlineFormSet):
    def clean(self):
        """
        Function to check that if there is a room already allotted.
        """
        cleaned_data = self.cleaned_data
        visitor_ = cleaned_data[0]['visitor']
        booked_rooms, booked_hostel, booked_type = get_zip_hostel_room(visitor_)
        for i in range(len(cleaned_data)):
            if cleaned_data[i].get('visitor') != visitor_:
                raise forms.ValidationError('ERROR')
            for r, h, t in itertools.zip_longest(booked_rooms, booked_hostel, booked_type):
                if str(cleaned_data[i].get('hostel_allotted')) == str(h):
                    if str(cleaned_data[i].get('room_no')) == str(r):
                        if str(cleaned_data[i].get('room_type')) == str(t):
                            raise forms.ValidationError('Room Already Allotted')
        return self.cleaned_data
