from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Boy, Room
from django.db import IntegrityError

@login_required
def add_boy(request):
    rooms = Room.objects.all()
    if request.method == "POST":
        try:
            room_id = request.POST.get("room")
            room = Room.objects.get(id=room_id)
            if room.boys.filter(is_active=True).count() >= Room.MAX_SEATS:
                messages.error(request, "Room is full!")
                return redirect("add_boy")
            Boy.objects.create(
                    room=room,
                    full_name=request.POST.get("full_name"),
                    father_name=request.POST.get("father_name"),
                    phone=request.POST.get("phone"),
                    cnic=request.POST.get("cnic"),
                    address=request.POST.get("address"),
                )
            messages.success(request, "Boy added successfully.")
            return redirect("boys_list")
        except IntegrityError:
            messages.error(request, "Ye CNIC pehle se mojood hai.")
            return redirect("add_boy")
    return render(request, "hostal/add_boy.html", {"rooms": rooms})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, "hostal/room_list.html", {"rooms": rooms})

def dashboard(request):

    total_rooms = Room.objects.count()
    total_boys = Boy.objects.filter(is_active=True).count()

    return render(request, "hostal/deshbaord.html", {
        "total_rooms": total_rooms,
        "total_boys": total_boys,
    })


def boys_list(request):
    boys = Boy.objects.all()
    return render(request, "hostal/boys_list.html", {"boys": boys})



@login_required
def edit_boy(request, id):

    boy = get_object_or_404(Boy, id=id)
    rooms = Room.objects.all()

    if request.method == "POST":

        boy.full_name = request.POST.get("full_name")
        boy.father_name = request.POST.get("father_name")
        boy.phone = request.POST.get("phone")
        boy.cnic = request.POST.get("cnic")
        boy.address = request.POST.get("address")
        boy.room_id = request.POST.get("room")

        boy.save()

        messages.success(request, "Boy updated successfully!")
        return redirect("boys_list")

    return render(request, "hostal/edit_boy.html", {
        "boy": boy,
        "rooms": rooms
    })

@login_required
def delete_boy(request, id):

    boy = get_object_or_404(Boy, id=id)

    boy.delete()

    messages.success(request, "Boy deleted successfully!")
    return redirect("boys_list")


