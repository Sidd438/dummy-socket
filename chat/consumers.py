import json
from .models import *
from django.db.models import Q
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatroomStatus(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "yessir"
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.send(text_data=json.dumps(text_data_json))

    async def get_message(self, event):
        await self.send(text_data=json.dumps(event))



class ChatroomDetailStatus(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "yessir"
        await self.channel_layer.group_add(str(self.room_group_name),self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.send(text_data=json.dumps(text_data_json))

    async def get_message(self, event):
        await database_sync_to_async(self.read_message)(event)
        await self.send(text_data=json.dumps(event))