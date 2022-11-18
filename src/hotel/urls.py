from django.urls import path
from .views import RoomList, BookingList, BookingForm


app_name = 'hotel'

urlpatterns = [ 
    path('room_list/', RoomList.as_view(), name='room-list-view'),
    # path('booking_list/', BookingList.as_view(), name=BookingList)
    path('book/', BookingForm.as_view(), name='book-view')
]