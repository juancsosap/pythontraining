import pygame as pg
from game import Game

from pingpong import handlers

class PingPong(Game):
    def __init__(self):
        super().__init__('Ping Pong', (500, 300))
        self.start()

    def init(self):
        super().init()

        self.register()

    def register(self):
        self.register_event(pg.QUIT, handlers.ChangeStatus(self, True))
