from django.urls import path
from .views import RoomListView, BookingList, BookingForm, RoomDetailView


app_name = 'hotel'

urlpatterns = [ 
    path('room_list/', RoomListView, name='room-list-view'),
    # path('booking_list/', BookingList.as_view(), name=BookingList),
    path('book/', BookingForm.as_view(), name='book-view'),
    path('room/<category>', RoomDetailView.as_view(), name='room-detail-view')
]