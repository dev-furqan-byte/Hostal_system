from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def signup(request):

    # Agar user pehle se login hai to dashboard par bhej d

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("login")

        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Account created successfully.")
        return redirect("login")

    return render(request, "accounts/signup.html")


def user_login(request):

    # Agar user pehle se login hai to dashboard par bhej do
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")
        return redirect("login")

    return render(request, "accounts/login.html")


def user_logout(request):

    logout(request)
    return redirect("login")