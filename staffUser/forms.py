from django import forms
from visitor.models import Visitor, BookingInfo
from django.contrib.auth import get_user_model
from django.forms.models import BaseInlineFormSet

User = get_user_model()


class CustomForm(forms.Form):
    status = forms.BooleanField(required=False)
    expired = forms.BooleanField(required=False)


class BooingAdminPanelForm(forms.ModelForm):
    class Meta:
        model = BookingInfo
        fields = ['hostel_allotted', 'room_no', 'room_type']


class booking_admin_panel_inline_form_base_form_set(BaseInlineFormSet):
    def clean(self):
        pass
