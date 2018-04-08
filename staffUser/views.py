from django.shortcuts import render
from visitor.models import Visitor, BookingInfo
from django.contrib.auth import get_user_model
from staffUser.forms import BooingAdminPanelForm, booking_admin_panel_inline_form_base_form_set, CustomForm
from django import forms

User = get_user_model()


def staff_homepage(request):
    visitor = Visitor.objects.all()
    return render(request, 'staffUser/index.html', {'visitor': visitor})


def user_request_edit_admin(request, id):
    user = User.objects.get(pk=id)
    visitor_obj = Visitor.objects.get(user=user)
    BookingAdminPanelInlineFormSet = forms.inlineformset_factory(Visitor, BookingInfo, form=BooingAdminPanelForm,
                                                                 extra=visitor_obj.no_of_rooms_required-1,
                                                                 can_delete=False,
                                                                 formset=booking_admin_panel_inline_form_base_form_set,
                                                                 )
    # if request.method == 'POST':
    #     form1 = CustomForm()
    #     form = BookingAdminPanelInlineFormSet(request.POST, instance=visitor_obj)
    #     print(request.POST)
    #     print(form.cleaned_data)
    # else:
    #     form = BookingAdminPanelInlineFormSet(instance=visitor_obj)
    if request.method == 'POST':
        form1 = BookingAdminPanelInlineFormSet(request.POST, instance=visitor_obj)
        form2 = CustomForm(request.POST)
        print(form1.cleaned_data)
        if form2.is_valid():
            print(form2.cleaned_data)
    else:
        form1 = BookingAdminPanelInlineFormSet(instance=visitor_obj)
        form2 = CustomForm
    return render(request, 'staffUser/edit.html', {'visitor_obj': visitor_obj, 'form1': form1, 'form2':form2})
