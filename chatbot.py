import asyncio
import time
import os
import aiohttp


class Chatbot:
    def __init__(self, **kwargs):
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])
        print(f"({self.id}) Instance created")
        self.username = self.config[self.id]['username']
        self.server = self.config['DEFAULT']['server']
        self.master = self.config[self.id]['master']
        self.queue = asyncio.Queue(loop=self.loop)
        self.teams = json.loads(self.config[self.id].get('teams'))
        self.rooms = {}
