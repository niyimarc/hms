from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Booking, Room
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability

# Create your views here.
class RoomList(ListView):
    model = Room
    template_name= 'hotel/room_list.html'

class BookingList(ListView):
    model = Booking
    template_name= ''

class BookingForm(FormView):
    form_class = AvailabilityForm
    template_name= 'hotel/availability_form.html'

    # this function is run after django check if the form is valid 
    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out'],
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('This category of rooms are booked.')

