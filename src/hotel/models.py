from django.db import models

# Create your models here.

ROOM_CATEGORIES = (
    ('Basic', 'Basic'),
    ('Diamond', 'Diamond'),
    ('Gold', 'Gold'),
    ('Silver', 'Silver')
)

class Room(models.Model):
    number = models.IntegerField()
    category = models.CharField(max_length=7, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} for {self.capacity} people'
