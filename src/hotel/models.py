from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Room(models.Model):
    ROOM_CATEGORIES = (
    ('Basic', 'Basic'),
    ('Diamond', 'Diamond'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver')
)
    number = models.IntegerField()
    category = models.CharField(max_length=7, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.user} has booked {self.room} from {self.check_in} to {self.check_out}"

