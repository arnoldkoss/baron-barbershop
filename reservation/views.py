from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

def book_reservation(request):
    """
    Renders the booking form and processes form submissions.
    """
    reserve_form = ReservationForm()  # Initialize the form

    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)  # Fill the form with data from the request
        if reserve_form.is_valid():  # Check if the form is valid
            reserve_form.save()  # Save the valid form/reservation
            # Optionally, you can redirect to a 'thank you' page or back to the form with a success message
            return redirect('book_reservation')  # Redirect to avoid double posting

    context = {'form': reserve_form}  # Prepare the context for rendering
    return render(request, "reservation/reservation.html", context)