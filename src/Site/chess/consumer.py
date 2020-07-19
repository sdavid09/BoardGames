import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer

class GameConsumer(AsyncConsumer):
    http_user=True
    async def websocket_connect(self, event):
        print("Connected", event)
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        msg = json.loads(event['text'])
        print("Receive", msg["message"])

        piece = {
            'message': msg["message"] ,
            'piece': "Rook"
        }
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(piece)
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
