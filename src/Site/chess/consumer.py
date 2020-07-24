import asyncio
from asgiref.sync import sync_to_async
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, JsonWebsocketConsumer

class GameConsumer(AsyncConsumer):
    http_user=True
    async def websocket_connect(self, event):
        print("Connected", event)
        game = "first"
        self.game = game
        await self.channel_layer.group_add(
            game,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        msg = json.loads(event['text'])
        print("Receive", msg)
        

        piece = {
            'message': msg ,
            'piece': "Rook"
        }
        # await self.send({
        #     "type": "websocket.send",
        #     "text": json.dumps(piece)
        # })
        await self.channel_layer.group_send(
            self.game,
            {
                "type": "custom_game",
                "text": json.dumps(piece)
             }

        )
    async def custom_game(self, event):
        print('message', event)
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
