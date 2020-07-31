import asyncio
from asgiref.sync import sync_to_async
from django.shortcuts import render, get_object_or_404
from .models import *
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
        first_piece = msg['firstPiece']
        second_piece = msg['secondPiece']

        piece = {
            'message': msg ,
            'piece': "Rook"
        }
        await self.move_piece(first_piece, second_piece)

        await self.channel_layer.group_send(
            self.game,
            {
                "type": "custom_game",
                "text": json.dumps(piece)
             }
        )

    @sync_to_async
    def move_piece(self, first_piece, second_piece):
        game = get_object_or_404(Game, id=1)
        first_piece_square = list(first_piece["square"])
        second_piece_square = list(second_piece["square"])
        first_piece_select = BoardSquare.objects.get(board=game.board, row=first_piece_square[1], column=first_piece_square[0])
        second_piece_select = BoardSquare.objects.get(board=game.board, row=second_piece_square[1], column=second_piece_square[0])
        first_player_piece = first_piece['id'].split('-')[1]
        piece = Piece.objects.get(pk=first_player_piece)
        second_piece_select.piece=piece
        second_piece_select.save()
        first_piece_select.piece=None
        first_piece_select.save()


    async def custom_game(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("Disconnected", event)
