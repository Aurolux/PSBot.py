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
        self.master = self.config[self.id]['master']
        self.rooms = {}
