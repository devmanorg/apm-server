import json
import asyncio

from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone

from .models import Play

SHORT_MEASUREMENT_SECS = 2
EXT_SHORT_MEASUREMENT_SECS = 5
LONG_MEASUREMENT_SECS = 30
FACTOR = 0.2


class PlayConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        play_id = self.scope['url_route']['kwargs']['play_id']
        play = get_object_or_404(Play, id=play_id)
        await self.accept()

        while True:
            now = timezone.now()

            elapsed = now - play.created
            short_apm = play.events.count_events(SHORT_MEASUREMENT_SECS) / SHORT_MEASUREMENT_SECS * 60
            ext_apm = play.events.count_events(EXT_SHORT_MEASUREMENT_SECS) / EXT_SHORT_MEASUREMENT_SECS * 60
            smoothed_apm = short_apm * FACTOR + ext_apm * (1 - FACTOR)

            average_apm = play.events.count_events(LONG_MEASUREMENT_SECS) / LONG_MEASUREMENT_SECS * 60

            await self.send(text_data=json.dumps({
                'current_apm': int(smoothed_apm),
                'average_apm': int(average_apm),
                'elapsed': [elapsed.seconds // 60, elapsed.seconds % 60],
            }))

            await asyncio.sleep(0.5)

    def disconnect(self, close_code):
        pass