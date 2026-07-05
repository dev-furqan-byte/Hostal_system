from django.db import models

from django.utils import timezone



class Room(models.Model):
    MAX_SEATS = 6
    room_number = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Room {self.room_number}"
    @property
    def available_seats(self):
        return self.MAX_SEATS - self.boys.count()
    @property
    def is_full(self):
        return self.boys.count() >= self.MAX_SEATS
class Boy(models.Model):
    room = models.ForeignKey(
        "Room",
        on_delete=models.SET_NULL,
        null=True,
        related_name="boys"
    )
    full_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    cnic = models.CharField(max_length=20, unique=True)
    address = models.TextField()
    joining_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name



