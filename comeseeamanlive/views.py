from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, "home.html", {
        "twitch_channel": settings.TWITCH_CHANNEL,
        "twitch_parent": settings.TWITCH_PARENT,
    })
