from django.contrib import admin
from .models import Visitor, BookingInfo
from visitor.forms import BookingInfoInlineAdminForm, VisitorAdminForm


class BookingInfoInline(admin.StackedInline):
    model = BookingInfo
    form = BookingInfoInlineAdminForm

    def get_extra(self, request, obj=None, **kwargs):
        if not obj is None:
            extra = obj.no_of_rooms_required
            return extra
        else:
            return 1

    def get_max_num(self, request, obj=None, **kwargs):
        if not obj is None:
            extra = obj.no_of_rooms_required
            return extra
        else:
            return 1

    def get_min_num(self, request, obj=None, **kwargs):
        if not obj is None:
            extra = obj.no_of_rooms_required
            return extra
        else:
            return 1


class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'no_of_rooms_required', 'status', 'date_of_booking', 'from_date', 'to_date', 'is_departed')
    inlines = [BookingInfoInline]
    form = VisitorAdminForm

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:
    #         temp = (
    #         'user',
    #         'no_of_rooms_required',
    #         'arrived_at',
    #         'departed_at',
    #         'from_date',
    #         'to_date',
    #         'date_of_booking'
    #         )
    #         return temp
    #     return self.readonly_fields

    fields = (
        'user',
        'no_of_rooms_required',
        'from_date',
        'to_date',
        'date_of_booking',
        'room_preference',
        'status',
        # 'is_arrived',
        # 'arrived_at',
        'is_departed',
        # 'departed_at'
    )


admin.site.register(Visitor, VisitorAdmin)
