import pygame as pg
import random
from game import Game, handlers as gh
from game.items import Rect, Text

from pingpong import handlers, items, actions

class PingPong(Game):
    def __init__(self, fps=30, factor=True):
        super().__init__('Ping Pong', (500, 300), (100, 60), fps=fps, resizable=True)
        self.factor = factor
        self.start()

    def init(self):
        super().init()

        self.borderg = 1
        self.playerheightg = 5
        
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
        self.draw_header()
        
        self.ball.draw(self.surface)
        
        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
                    
    def draw_bg(self):
        widthg, heightg = self.gridshape
        borderg = self.borderg

        self.surface.fill(pg.Color('purple'))
        
        xg, yg = self.borderg, self.borderg * 2 + self.playerheightg
        rwidthg, rheightg = widthg - borderg * 2, heightg - borderg * 3 - self.playerheightg
        Rect(self, xg, yg, rwidthg, rheightg, pg.Color('white')).draw(self.surface)
    
    def draw_header(self):
        textwidthg = self.gridshape[0] - self.borderg * 2

        txt = " Player 1 : {}".format(self.player1.points)
        Text(self, txt, pg.Color('black'), self.borderg, self.borderg).setalign('left', 'center') \
            .setrect(textwidthg, self.playerheightg).draw(self.surface)
                
        txt = "{} : Player 2 ".format(self.player2.points)
        Text(self, txt, pg.Color('black'), self.borderg, self.borderg).setalign('right', 'center') \
            .setrect(textwidthg, self.playerheightg).draw(self.surface)
        