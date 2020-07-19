import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer

class GameConsumer(JsonWebsocketConsumer):
    http_user=True

    def connect(self):
        print("Connected")
        super(GameConsumer, self).connect()
        self.send(
            text_data=json.dumps({
                'type': 'connect'
            })
        )


    def receive(self, message, **kwargs):
        print("Receive", message)

    def disconnect(self, message, **kwargs):
        print("Disconnected", message)
