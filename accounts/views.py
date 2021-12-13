from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserCreationForm

# Create your views here.


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, "accounts/signup.html", {"form": form})
