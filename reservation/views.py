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
            reserve_form.save()
            messages.success(request,"successfull reservation")  
            
            return redirect('reservation') 

    context = {'form': reserve_form}  
    return render(request, "reservation/reservation.html", context)