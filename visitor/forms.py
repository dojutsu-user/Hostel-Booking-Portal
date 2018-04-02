from django import forms
from hostel.models import Hostel


class VisitorAdminForm(forms.ModelForm):
    def clean_hostel_allotted(self):
        allotted_hostel = self.cleaned_data.get('hostel_allotted')
        available_rooms = Hostel.objects.get(name=allotted_hostel).available_rooms()
        # if self.no_of_rooms_required >

