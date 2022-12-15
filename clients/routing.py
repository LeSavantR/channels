from django.urls import path

from clients.consumers import ChatConsumer



websocket_urlpatterns = [
    path('ws/socket-server/', ChatConsumer.as_asgi(), name='connection')
]