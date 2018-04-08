from django import forms
from visitor.models import Visitor
from django.utils import timezone
from visitor.util import total_rooms


class EditRequests(forms.ModelForm):
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
