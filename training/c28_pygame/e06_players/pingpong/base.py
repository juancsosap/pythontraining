import pygame as pg
from game import Game, items

from pingpong import handlers, players

class PingPong(Game):
    def __init__(self):
        super().__init__('Ping Pong', (500, 300))
        self.start()

    def init(self):
        super().init()

        self.player1 = players.Player(15, 150, pg.Color('red'))
        self.player2 = players.Player(485, 150, pg.Color('red'))

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

        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
    
    def draw_bg(self):
        rect = (self.border, self.border, self.size[0] - 2 * self.border, self.size[1] - 2 * self.border)
        self.surface.fill(pg.Color('purple'))
        self.surface.fill(pg.Color('white'), rect=rect)
