import random
import pygame as pg
from game import GameWindow, handlers as gh
from game.items import Rect, Text
from game.controls import Button

from pingpong import handlers, items, actions

class IntroWindow(GameWindow):
    def init(self):
        super().init()
        
        self.borderg = self.game.borderg
        
        self.register()

    def register(self):
        handler = gh.KeyDone(self.game, (pg.K_q, pg.K_ESCAPE), 'exit')
        self.register_event(pg.KEYDOWN, handler)
        
        handler = gh.KeyDone(self.game, (pg.K_s, pg.K_RETURN), 'start')
        self.register_event(pg.KEYDOWN, handler)
        
        self.register_event(pg.VIDEORESIZE, handlers.ResizeInfoWindow(self.game))
        
    def initialdraw(self):
        self.draw_bg()

        widthg, heightg = self.game.gridshape
        textwidthg = widthg - self.borderg * 2

        Text(self, "Ping Pong", pg.Color('red'), self.borderg, self.borderg).setalign('center', 'center') \
            .setfont(None, 20).setrect(textwidthg, heightg // 2 - self.borderg).draw(self.surface)
                
        txt = "Press P to pause the game"
        Text(self, txt, pg.Color('black'), self.borderg, 5 * heightg // 6).setalign('center', 'top') \
            .setfont(None, 7).setrect(textwidthg, heightg // 6 - self.borderg).draw(self.surface)
        
        colors = [pg.Color('red'), pg.Color('pink'), pg.Color('purple'), pg.Color('black')]
        Button(self, widthg * 1/4, heightg * 7/12, widthg * 1/6, 10, colors, "ENTER", None).draw(self.surface)
        Button(self, widthg * 7/12, heightg * 7/12, widthg * 1/6, 10, colors, "EXIT", None).draw(self.surface)
            
    def draw_bg(self):
        self.surface.fill(pg.Color('purple'))
        
        widthg, heightg = self.game.gridshape
        borderg = self.borderg

        xg, yg = self.borderg, self.borderg
        rwidthg, rheightg = widthg - borderg * 2, heightg - borderg * 2
        Rect(self, xg, yg, rwidthg, rheightg, pg.Color('white')).draw(self.surface)
    

class PauseWindow(GameWindow):
    def init(self):
        super().init()

        self.borderg = self.game.borderg
        self.restart = False

        self.register()

    def register(self):
        handler = gh.KeyDone(self.game, (pg.K_q, pg.K_ESCAPE), 'exit')
        self.register_event(pg.KEYDOWN, handler)
        
        handler = gh.KeyDone(self.game, (pg.K_r, pg.K_SPACE), 'start')
        self.register_event(pg.KEYDOWN, handler)
        
        handler = gh.KeyDone(self.game, (pg.K_c, pg.K_RETURN), 'continue')
        self.register_event(pg.KEYDOWN, handler)
        
        self.register_event(pg.VIDEORESIZE, handlers.ResizeInfoWindow(self.game))
        
    def initialdraw(self):
        self.draw_bg()

        widthg, heightg = self.game.gridshape
        textwidthg = widthg - self.borderg * 2

        Text(self, "Ping Pong", pg.Color('red'), self.borderg, self.borderg).setalign('center', 'center') \
            .setfont(None, 20).setrect(textwidthg, heightg // 2 - self.borderg).draw(self.surface)
                
        txt = "Press R or SPACE to restart the game"
        Text(self, txt, pg.Color('black'), self.borderg, heightg // 2).setalign('center', 'top') \
            .setfont(None, 7).setrect(textwidthg, heightg // 6).draw(self.surface)

        txt = "Press C or ENTER to continue the game"
        Text(self, txt, pg.Color('black'), self.borderg, 2 * heightg // 3).setalign('center', 'top') \
            .setfont(None, 7).setrect(textwidthg, heightg // 6).draw(self.surface)

        txt = "Press Q or ESCAPE to exit the game"
        Text(self, txt, pg.Color('black'), self.borderg, 5 * heightg // 6).setalign('center', 'top') \
            .setfont(None, 7).setrect(textwidthg, heightg // 6 - self.borderg).draw(self.surface)
            
    def draw_bg(self):
        self.surface.fill(pg.Color('purple'))
        
        widthg, heightg = self.game.gridshape
        borderg = self.borderg

        xg, yg = self.borderg, self.borderg
        rwidthg, rheightg = widthg - borderg * 2, heightg - borderg * 2
        Rect(self, xg, yg, rwidthg, rheightg, pg.Color('white')).draw(self.surface)


class MainWindow(GameWindow):
    def init(self):
        super().init()

        self.borderg = self.game.borderg
        self.playerheightg = 5
        
        self.player1 = items.Player(self, 3, 25, 2, 10, pg.Color('red'))
        self.player2 = items.Player(self, 95, 25, 2, 10, pg.Color('red'))

        self.ball = items.Ball(self, 2, pg.Color('blue'))
        
        self.register()

    def register(self):
        handler = gh.KeyActionHandler(self.game, (pg.K_w,), self.player1, actions.MoveUp)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)
        
        handler = gh.KeyActionHandler(self.game, (pg.K_z,), self.player1, actions.MoveDown)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        handler = gh.KeyActionHandler(self.game, (pg.K_UP,), self.player2, actions.MoveUp)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        handler = gh.KeyActionHandler(self.game, (pg.K_DOWN,), self.player2, actions.MoveDown)
        self.register_event(pg.KEYDOWN, handler, pg.KEYUP)

        self.register_actions(actions.MoveBall(self.game, self.ball))

        self.register_event(pg.VIDEORESIZE, handlers.ResizeMainWindow(self.game))

        handler = gh.KeyDone(self.game, (pg.K_p,), 'pause')
        self.register_event(pg.KEYDOWN, handler)

    def initialdraw(self):
        pass

    def redraw(self):
        self.draw_bg()
        self.draw_header()
        
        self.ball.draw(self.surface)
        
        self.player1.draw(self.surface)
        self.player2.draw(self.surface)
                    
    def draw_bg(self):
        widthg, heightg = self.game.gridshape
        borderg = self.borderg

        self.surface.fill(pg.Color('purple'))
        
        xg, yg = self.borderg, self.borderg * 2 + self.playerheightg
        rwidthg, rheightg = widthg - borderg * 2, heightg - borderg * 3 - self.playerheightg
        Rect(self, xg, yg, rwidthg, rheightg, pg.Color('white')).draw(self.surface)
    
    def draw_header(self):
        textwidthg = self.game.gridshape[0] - self.borderg * 2

        txt = " Player 1 : {}".format(self.player1.points)
        Text(self, txt, pg.Color('black'), self.borderg, self.borderg).setalign('left', 'center') \
            .setrect(textwidthg, self.playerheightg).draw(self.surface)
                
        txt = "{} : Player 2 ".format(self.player2.points)
        Text(self, txt, pg.Color('black'), self.borderg, self.borderg).setalign('right', 'center') \
            .setrect(textwidthg, self.playerheightg).draw(self.surface)
