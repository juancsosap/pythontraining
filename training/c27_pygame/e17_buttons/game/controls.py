import pygame as pg
from game.items import Item, Rect, Ellipse

class Control(Item):
    def __init__(self, gamewindow, xg, yg, widthg, heightg, colors, text, action):
        super().__init__(gamewindow, xg, yg, widthg, heightg)
        self.state = 'normal'

    def register(self):
        pass

    def iswithin(self):
        pass 
    

class Button(Control):
    def __init__(self, gamewindow, xg, yg, widthg, heightg, colors, text, action):
        super().__init__(gamewindow, xg, yg, widthg, heightg)
        self.colors = colors
        self.text = text
        self.action = action

        self.register()
    
    def draw(self, surface):
        if self.state == 'normal': color = self.colors[0]
        elif self.state == 'over': color = self.colors[1]
        elif self.state == 'down': color =  self.colors[2]

        Rect(self.gamewindow, self.xg, self.yg, self.widthg, self.heightg, color).draw(surface)
        Text(self.gamewindow, self.text, self.color[3], self.xg, self.yg).setalign('center', 'center') \
            .setrect(self.widthg, self.heightg).draw(surface)

    def register(self):
        handler = handlers.ControlMouseOverHandler(self.game, self, {'normal':'over', 'over':'over', 'down':'down'})
        self.gamewindow.register_event(pg.MOUSEMOTION, handler)
        handler = handlers.ControlMouseButtonHandler(self.game, self, 1, {'normal':'down', 'over':'down'})
        self.gamewindow.register_event(pg.MOUSEBUTTONDOWN, handler)
        handler = handlers.ControlMouseButtonHandler(self.game, self, 1, {'normal':'over', 'over':'over', 'down':'over'})
        self.gamewindow.register_event(pg.MOUSEBUTTONUP, handler)
    
    def iswithin(self, pos):
        xg, yg = self.ungrid(*pos)
        withinx = xg >= self.xg and xg <= self.xg + self.widthg
        withiny = yg >= self.yg and yg <= self.yg + self.heightg
        return withinx and withiny