from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import Room, Boy


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("room_number", "created_at")


@admin.register(Boy)
class BoyAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "room",
        "phone",
        "joining_date",
        "is_active",
    )

    search_fields = (
        "full_name",
        "phone",
        "cnic",
    )

    list_filter = (
        "room",
        "is_active",
    )





