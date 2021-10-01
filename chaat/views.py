from django.http import request
from django.shortcuts import render


def main_view(request):
    return render(request, "chaat/index.html", {})


def chaat_room_view(request, room_name):
    return render(request, "chaat/room.html", {
        'room_name': room_name
    })
