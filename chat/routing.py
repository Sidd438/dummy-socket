from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chatroom/collection/',consumers.ChatroomStatus.as_asgi()),
    path('ws/chatroom/detail/<str:chatroom_id>/',consumers.ChatroomDetailStatus.as_asgi()),
]