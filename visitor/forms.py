from django import forms
from visitor.models import Visitor
from visitor.util import total_rooms


class BookARoom(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['no_of_rooms_required']

    def clean_no_of_rooms_required(self):
        rooms = total_rooms()
        required_rooms = self.cleaned_data.get('no_of_rooms_required')
        if required_rooms > rooms:
            raise forms.ValidationError("Required Rooms Are Not Available")
        elif required_rooms <= 0:
            raise forms.ValidationError("Please Enter Correct Value")
        return required_rooms

