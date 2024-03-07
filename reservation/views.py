from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages

def book_reservation(request):
    """
    Renders the booking form and processes form submissions.
    """
    reserve_form = ReservationForm()
    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reservation = reserve_form.save(commit=False)
            booking_details_message = f"Reservation confirmed for {reservation.date} at {reservation.time}."
            reservation.save()
            messages.success(request, booking_details_message)  
            return redirect('reservation') 
    context = {'form': reserve_form}
    return render(request, "reservation/reservation.html", context)