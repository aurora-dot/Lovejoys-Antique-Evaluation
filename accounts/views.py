from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserCreationForm

# Create your views here.


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.email = form.cleaned_data.get("email")
        user.profile.phone_number = form.cleaned_data.get("phone_number")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/signup.html", {"form": form})
