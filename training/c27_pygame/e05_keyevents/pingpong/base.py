import pygame as pg
from game import Game, items

from pingpong import handlers

class PingPong(Game):
    def __init__(self):
        super().__init__('Ping Pong', (500, 300))
        self.start()

    def init(self):
        super().init()

        self.border = 5
        
        self.register()

    def register(self):
        self.register_event(pg.QUIT, handlers.ChangeStatus(self, True))
        
        keys = (pg.K_UP, pg.K_DOWN, pg.K_w, pg.K_z)
        self.register_event(pg.KEYDOWN, handlers.KeyPrinter(self, keys))
        self.register_event(pg.KEYDOWN, handlers.KeyPrinter(self, (pg.K_SPACE,)))

    def redraw(self):
        self.draw_bg()
        
        items.Circle(250, 150, 10, pg.Color('blue')).draw(self.surface)
        items.Rect(10, 125, 10, 50, pg.Color('red')).draw(self.surface)
        items.Rect(480, 125, 10, 50, pg.Color('green')).draw(self.surface)
    
    def draw_bg(self):
        rect = (self.border, self.border, self.size[0] - 2 * self.border, self.size[1] - 2 * self.border)
        self.surface.fill(pg.Color('purple'))
        self.surface.fill(pg.Color('white'), rect=rect)
    