from django import forms
from visitor.models import Visitor
from visitor.util import total_rooms
from django.utils import timezone


class BookARoom(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['no_of_rooms_required', 'from_date', 'to_date']
        widgets = {
            'from_date': forms.SelectDateWidget(),
            'to_date': forms.SelectDateWidget(),
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
