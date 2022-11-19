from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, DetailView
from .models import Booking, Room
from .forms import AvailabilityForm
from hotel.booking_functions.availability import check_availability
from django.urls import reverse

# Create your views here.
def RoomListView(request):
    # select the first room 
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)

    # create an empty room_list 
    room_list = []

    # loop through the room_categories dictionary 
    for room_category in room_categories:
        room = room_categories.get(room_category)
        room_url = reverse('hotel:room-detail-view', kwargs={
                                'category': room_category})

        # append room and room_url to the room_list 
        room_list.append((room, room_url))
        
    contex ={
        "room_list":room_list,
    }  
    return render(request, 'hotel/room_list.html', contex)

class RoomDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        # filter the Room model by category the user selected 
        room_list = Room.objects.filter(category=category)


        # run the code below if there is data in room_list 
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            contex = {
                'room_category': room_category,
            }
            return render(request, 'hotel/room_detail.html', contex)
        else:
            return HttpResponse('Category doesnt exist')


    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        # filter the Room model by category the user selected 
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data =form.cleaned_data

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

