from django.contrib import admin
from .models import Visitor, BookingInfo
from visitor.forms import BookingInfoInlineAdminForm


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
    list_display = ('user', 'no_of_rooms_required', 'status', 'date_of_booking', 'from_date', 'to_date')
    inlines = [BookingInfoInline]


admin.site.register(Visitor, VisitorAdmin)
