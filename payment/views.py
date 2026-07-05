from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .models import Payment
from hostal.models import Boy

# Create your views here.
from django.db import IntegrityError

@login_required
def add_payment(request):

    boys = Boy.objects.filter(is_active=True)

    if request.method == "POST":

        boy_id = request.POST.get("boy")
        boy = Boy.objects.get(id=boy_id)

        try:
            Payment.objects.create(
                boy=boy,
                month=request.POST.get("month"),
                year=request.POST.get("year"),
                advance=request.POST.get("advance"),
                rent=request.POST.get("rent"),
                status=request.POST.get("status"),
            )

            messages.success(request, "Payment added successfully!")
            return redirect("payment_list")

        except IntegrityError:
            messages.error(request, "Same person ki same month aur year ki payment pehle se mojood hai.")
            return redirect("add_payment")

    return render(request, "payment/add_payment.html", {"boys": boys})

def payment_list(request):

    payments = Payment.objects.all().order_by("-created_at")

    return render(request, "payment/payment_list.html", {"payments": payments})



@login_required
def edit_payment(request, id):

    payment = get_object_or_404(Payment, id=id)
    boys = Boy.objects.filter(is_active=True)

    if request.method == "POST":

        payment.boy_id = request.POST.get("boy")
        payment.month = request.POST.get("month")
        payment.year = request.POST.get("year")
        payment.advance = request.POST.get("advance")
        payment.rent = request.POST.get("rent")
        payment.status = request.POST.get("status")

        payment.save()

        messages.success(request, "Payment updated successfully!")
        return redirect("payment_list")

    return render(request, "payment/payment_edit.html", {
        "payment": payment,
        "boys": boys
    })

@login_required
def delete_payment(request, id):

    payment = get_object_or_404(Payment, id=id)

    payment.delete()

    messages.success(request, "Payment deleted successfully!")

    return redirect("payment_list")