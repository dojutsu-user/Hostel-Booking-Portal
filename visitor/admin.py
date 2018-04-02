from django.contrib import admin
from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('user', 'no_of_rooms_required', 'status', 'date_of_booking')


admin.site.register(Visitor, VisitorAdmin)
