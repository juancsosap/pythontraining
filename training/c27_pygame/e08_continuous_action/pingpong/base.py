import pygame as pg
from game import Game, handlers as gh

from pingpong import handlers, items, actions

class PingPong(Game):
    def __init__(self):
        super().__init__('Ping Pong', (500, 300))
        self.start()

    def init(self):
        super().init()

        self.player1 = items.Player(15, 150, pg.Color('red'))
        self.player2 = items.Player(485, 150, pg.Color('red'))
        self.ball = items.Ball(250, 150, 10, pg.Color('blue'))

        self.grid = 5
        self.border = 5
        
        self.register()
        
    def register(self):
        self.register_event(pg.QUIT, handlers.ChangeStatus(self, True))
        
        self.register_event(pg.KEYDOWN, handlers.MoveUp(self, (pg.K_w,), self.player1))
        self.register_event(pg.KEYDOWN, handlers.MoveDown(self, (pg.K_z,), self.player1))
        self.register_event(pg.KEYDOWN, handlers.MoveUp(self, (pg.K_UP,), self.player2))
        self.register_event(pg.KEYDOWN, handlers.MoveDown(self, (pg.K_DOWN,), self.player2))

        self.register_actions(actions.MoveBall(self, self.ball))

    def redraw(self):
        self.draw_bg()
        
        self.ball.draw(self.surface)

        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
    
    def draw_bg(self):
        rect = (self.border, self.border, self.size[0] - 2 * self.border, self.size[1] - 2 * self.border)
        self.surface.fill(pg.Color('purple'))
        self.surface.fill(pg.Color('white'), rect=rect)
