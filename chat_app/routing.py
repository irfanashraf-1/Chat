from django.urls import path
from .consumers import ChatConsumer

ws_urlpatterns = [
    path('ws/messages/<str:room_name>/', ChatConsumer.as_asgi()),
]