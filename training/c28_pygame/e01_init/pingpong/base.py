import pygame as pg
from game import Game

class PingPong(Game):
    def __init__(self):
        super().__init__('Ping Pong', (500, 300), 5000) # 5 Seconds
        self.start()
