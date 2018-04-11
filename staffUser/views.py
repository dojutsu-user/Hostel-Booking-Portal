from django.shortcuts import render
from visitor.models import Visitor, BookingInfo
from django.contrib.auth import get_user_model
from staffUser.forms import BooingAdminPanelForm, booking_admin_panel_inline_form_base_form_set
from django import forms
from hostel.models import Hostel
from django.urls import reverse
from django.http import HttpResponseRedirect

User = get_user_model()


def staff_homepage(request):
    visitor = Visitor.objects.all()
    return render(request, 'staffUser/index.html', {'visitor': visitor})


def user_request_edit_admin(request, id):
    user = User.objects.get(pk=id)
    visitor_obj = Visitor.objects.get(user=user)
    BookingAdminPanelInlineFormSet = forms.inlineformset_factory(Visitor, BookingInfo, form=BooingAdminPanelForm,
                                                                 extra=visitor_obj.no_of_rooms_required,
                                                                 max_num=visitor_obj.no_of_rooms_required,
                                                                 min_num=visitor_obj.no_of_rooms_required,
                                                                 can_delete=False,
                                                                 formset=booking_admin_panel_inline_form_base_form_set,
                                                                 )
    if request.method == 'POST':
        form = BookingAdminPanelInlineFormSet(request.POST, instance=visitor_obj)
        if form.is_valid():
            form.save()
    else:
        form = BookingAdminPanelInlineFormSet(instance=visitor_obj)
    return render(request, 'staffUser/edit.html', {'visitor_obj': visitor_obj, 'form': form})


def change_status(request, id):
    visitor_obj = Visitor.objects.get(pk=id)
    VH1 = Hostel.objects.get(name__icontains='VH1')
    VH2 = Hostel.objects.get(name__icontains='VH2')
    VH3 = Hostel.objects.get(name__icontains='VH3')
    if not visitor_obj.status:
        booking_info = BookingInfo.objects.filter(visitor=visitor_obj)
        for info in booking_info:
            hostel_allotted = info.hostel_allotted
            print(hostel_allotted)
            if hostel_allotted == '1':
                VH1.total_available_rooms -= 1
                VH1.total_booked_rooms += 1
                VH1.save()
            elif hostel_allotted == '2':
                VH2.total_available_rooms -= 1
                VH2.total_booked_rooms += 1
                VH2.save()
            elif hostel_allotted == '3':
                VH3.total_available_rooms -= 1
                VH3.total_booked_rooms += 1
                VH3.save()
        visitor_obj.status = True
        visitor_obj.save()
    else:
        booking_info = BookingInfo.objects.filter(visitor=visitor_obj)
        for info in booking_info:
            hostel_allotted = info.hostel_allotted
            print(hostel_allotted)
            if hostel_allotted == '1':
                VH1.total_available_rooms += 1
                VH1.total_booked_rooms -= 1
                VH1.save()
            elif hostel_allotted == '2':
                VH2.total_available_rooms += 1
                VH2.total_booked_rooms -= 1
                VH2.save()
            elif hostel_allotted == '3':
                VH3.total_available_rooms += 1
                VH3.total_booked_rooms -= 1
                VH3.save()
        visitor_obj.status = False
        visitor_obj.save()
    return HttpResponseRedirect(reverse('user_request_edit_admin', args=[visitor_obj.user.id]))
