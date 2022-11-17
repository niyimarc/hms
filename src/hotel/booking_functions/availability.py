from hotel.models import Room, Booking
import datetime

# this will check if room is available from the time the user input 
def check_availability(room, check_in, check_out):
    avail_list = []
    # filter the objects from Booking with the room 
    booking_list = Booking.objects.filter(room=room)
    for b in booking_list:
        if b.check_in > b.check_out or b.check_out < b.check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
        # all() function return True 
        # if all the list are True 
        return all(avail_list)
