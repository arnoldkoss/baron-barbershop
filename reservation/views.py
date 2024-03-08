from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


def book_reservation(request):
    """
    View function for handling reservation bookings.

    This function renders a reservation form
    (`ReservationForm`) for GET requests
    and processes the form for POST requests. If the form submission is valid,
    it saves a new `Reservation` instance,
    displays a success message with the booking
    details, and redirects to a specified URL
    (assumed to be named 'reservation').
    """
    reserve_form = ReservationForm()
    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reservation = reserve_form.save(commit=False)
            booking_details_message = (
                f"Reservation confirmed for {reservation.date} "
                f"at {reservation.time}."
            )
            reservation.save()
            messages.success(request, booking_details_message)
            return redirect('reservation')
    context = {'form': reserve_form}
    return render(request, "reservation/reservation.html", context)
