from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Admin class for the Reservation model.

    This class specifies how the Reservation model should be displayed in the Django admin interface.
    It customizes the list display to include certain fields.
    """
    list_display = ['name', 'date', 'time', 'gender']
