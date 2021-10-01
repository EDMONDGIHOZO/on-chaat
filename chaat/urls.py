from django.urls import path

from chaat.views import main_view, chaat_room_view

urlpatterns = [
    path('', main_view, name='main'),
    path('<str:room_name>/', chaat_room_view, name='room')
]
