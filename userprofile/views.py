from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect("frontpage")
    else:
        form = UserCreationForm()

    return render(request, "userprofile/signup.html", {"form": form})
