from django.shortcuts import render
from .models import Reservation


def book_reservation(request):
    """
    Renders the Reservation page
    """
    reservation = Reservation.objects.all().order_by('-date', '-time', '-gender').first()

    return render(
        request,
        "reservation/reservation.html",
        {"reservation": reservation},
    )