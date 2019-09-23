import pygame as pg
# pip install pygame

class Item:
    def __init__(self, game):
        self.game = game
        self.xg, self.yg = 0, 0
        self.widthg, self.heightg = 0, 0

    def grid(self, xg, yg):
        return (self.gridx(xg), self.gridy(yg)) 

    def gridx(self, xg):
        return xg * self.game.size[0] / self.game.gridshape[0] 

    def gridy(self, yg):
        return yg * self.game.size[1] / self.game.gridshape[1] 

    def draw(self, surface):
        pass

    def prepare(self):
        pass

    def resize(self, oldgridshape, newgirdshape):
        pass

    def iswithin(self, other):
        withinx = self.xg <= other.xg + other.widthg and \
                  self.xg + self.widthg >= other.xg 
        withiny = self.yg <= other.yg + other.heightg and \
                  self.yg + self.heightg >= other.yg
        return withinx and withiny 

class Rect(Item):
    def __init__(self, game, xg, yg, widthg, heightg, color):
        super().__init__(game)

        self.xg, self.yg = xg, yg
        self.widthg, self.heightg = widthg, heightg
        self.color = color

    def draw(self, surface):
        self.prepare()
        pg.draw.rect(surface, self.color, self.rect)

    def prepare(self):
        x, y = self.grid(self.xg, self.yg)
        width, height = self.grid(self.widthg, self.heightg)
        self.rect = (x, y, width, height)

class Ellipse(Rect):
    def draw(self, surface):
        self.prepare()
        pg.draw.ellipse(surface, self.color, self.rect)

class Circle(Item):
    def __init__(self, game, xg, yg, radiusg, color):
        super().__init__(game)

        self.centerg = xg, yg
        self.radiusg = radiusg
        self.color = color

        self.xg, self.yg = self.centerg[0] - self.radiusg, self.centerg[1] - self.radiusg
        self.widthg, self.heightg = self.radiusg * 2, self.radiusg * 2

    def draw(self, surface):
        self.prepare()
        pg.draw.ellipse(surface, self.color, self.rect)

    def prepare(self):
        self.xg, self.yg = self.centerg[0] - self.radiusg, self.centerg[1] - self.radiusg
        self.widthg, self.heightg = self.radiusg * 2, self.radiusg * 2
        self.center = self.grid(*self.centerg)
        self.radius = self.grid(self.radiusg, self.radiusg)
        self.x, self.y = self.center[0] - self.radius[0], self.center[1] - self.radius[1]
        self.rect = self.x, self.y, self.radius[0] * 2, self.radius[1] * 2

class HLine(Item):
    def __init__(self, game, xg_ini, xg_end, yg, widthg, color):
        super().__init__(game)

        self.inig, self.endg = xg_ini, xg_end
        self.yg = yg
        self.widthg = widthg
        self.color = color

    def draw(self, surface):
        self.prepare()
        pg.draw.line(surface, self.color, self.ini, self.end, self.width)

    def prepare(self):
        y = self.gridy(self.yg)
        self.ini = self.gridx(self.inig), y  
        self.end = self.gridx(self.endg), y
        self.width = self.gridy(self.widthg)

class VLine(Item):
    def __init__(self, game, xg, yg_ini, yg_end, widthg, color):
        super().__init__(game)

        self.xg = xg
        self.inig, self.endg = yg_ini, yg_end
        self.widthg = widthg
        self.color = color

    def draw(self, surface):
        self.prepare()
        pg.draw.line(surface, self.color, self.ini, self.end, self.width)

    def prepare(self):
        x = self.gridx(self.xg)
        self.ini = x, self.gridy(self.inig)  
        self.end = x, self.gridy(self.endg)
        self.width = self.gridx(self.widthg)

class Player(Item):
    def __init__(self, game, xg, yg, widthg, heightg):
        super().__init__(game)

        self.xg, self.yg = xg, yg
        self.widthg, self.heightg = widthg, heightg
