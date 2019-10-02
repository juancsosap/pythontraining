import pygame as pg
import random
from game import Game, handlers as gh
from game.items import Rect

from pingpong import handlers, items, actions

class PingPong(Game):
    def __init__(self, fps=30, factor=True):
        super().__init__('Ping Pong', (500, 300), (100, 60), fps=fps, resizable=True)
        self.factor = factor
        self.start()

    def init(self):
        super().init()

        self.borderg = 1
        
        self.player1 = items.Player(self, 3, 25, 2, 10, pg.Color('red'))
        self.player2 = items.Player(self, 95, 25, 2, 10, pg.Color('red'))

        self.ball = items.Ball(self, 2, pg.Color('blue'))
        
        self.register()
        
    def register(self):
        self.register_event(pg.QUIT, handlers.ChangeStatus(self, True))
        
        handler = gh.KeyActionHandler(self, (pg.K_w,), self.player1, actions.MoveUp)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)
        
        handler = gh.KeyActionHandler(self, (pg.K_z,), self.player1, actions.MoveDown)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        handler = gh.KeyActionHandler(self, (pg.K_UP,), self.player2, actions.MoveUp)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        handler = gh.KeyActionHandler(self, (pg.K_DOWN,), self.player2, actions.MoveDown)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        self.register_actions(actions.MoveBall(self, self.ball))

        self.register_event(pg.VIDEORESIZE, handlers.ResizeWindow(self))
        
    def redraw(self):
        self.draw_bg()
        
        self.ball.draw(self.surface)
        
        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
    
    def draw_bg(self):
        self.surface.fill(pg.Color('purple'))
        Rect(self, self.borderg, self.borderg, self.gridshape[0] - self.borderg * 2, 
                   self.gridshape[1] - self.borderg * 2, pg.Color('white')).draw(self.surface)
