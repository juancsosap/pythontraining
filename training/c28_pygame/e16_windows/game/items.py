import pygame as pg
# pip install pygame

class Item:
    def __init__(self, gamewindow, xg=0, yg=0, widthg=0, heightg=0):
        self.gamewindow = gamewindow
        self.xg, self.yg = xg, yg
        self.widthg, self.heightg = widthg, heightg

    def grid(self, xg, yg):
        return (self.gridx(xg), self.gridy(yg)) 

    def gridx(self, xg):
        return xg * self.gamewindow.game.size[0] / self.gamewindow.game.gridshape[0] 

    def gridy(self, yg):
        return yg * self.gamewindow.game.size[1] / self.gamewindow.game.gridshape[1] 

    def ungrid(self, x, y):
        return (self.ungridx(x), self.ungridy(y)) 

    def ungridx(self, x):
        return x * self.gamewindow.game.gridshape[0] / self.gamewindow.game.size[0] 

    def ungridy(self, y):
        return y * self.gamewindow.game.gridshape[1] / self.gamewindow.game.size[1] 

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
    def __init__(self, gamewindow, xg, yg, widthg, heightg, color):
        super().__init__(gamewindow, xg, yg, widthg, heightg)

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
    def __init__(self, gamewindow, xg, yg, radiusg, color):
        super().__init__(gamewindow)

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
    def __init__(self, gamewindow, xg_ini, xg_end, yg, linewidthg, color):
        super().__init__(gamewindow, xg_ini, yg, xg_end - xg_ini, linewidthg)

        self.inig, self.endg = xg_ini, xg_end
        self.heightg = linewidthg
        self.color = color

    def draw(self, surface):
        self.prepare()
        pg.draw.line(surface, self.color, self.ini, self.end, self.height)

    def prepare(self):
        y = self.gridy(self.yg)
        self.ini = self.gridx(self.inig), y  
        self.end = self.gridx(self.endg), y
        self.height = self.gridy(self.heightg)

class VLine(Item):
    def __init__(self, gamewindow, xg, yg_ini, yg_end, linewidthg, color):
        super().__init__(gamewindow, xg, yg_ini, linewidthg, yg_end - yg_ini)

        self.inig, self.endg = yg_ini, yg_end
        self.widthg = linewidthg
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
    def __init__(self, gamewindow, xg, yg, widthg, heightg):
        super().__init__(gamewindow)

        self.xg, self.yg = xg, yg
        self.widthg, self.heightg = widthg, heightg

class Text(Item):
    def __init__(self, gamewindow, text, color, xg, yg):
        super().__init__(gamewindow, xg, yg)

        self.text = text
        self.fgcolor = color
        self.align = ('left', 'top')
        
        self.setfont(None, 5) # "comicsans"

    def setfont(self, fonttype, sizeg):
        self.fonttype = fonttype
        self.sizeg = sizeg
        return self
    
    def setalign(self, halign, valign):
        self.align = (halign, valign)
        return self

    def setrect(self, widthg, heightg):
        self.widthg, self.heightg = widthg, heightg
        return self

    def draw(self, surface):
        self.prepare()
        surface.blit(self.textsurface, self.rect)

    def prepare(self):
        size = int(self.gridy(self.sizeg))
        self.font = pg.font.SysFont(self.fonttype, size)
        self.textsurface = self.font.render(self.text, True, self.fgcolor)
        textwidth, textheight = self.textsurface.get_size()
        
        x, y = self.grid(self.xg, self.yg)
        width, height = self.grid(self.widthg, self.heightg)
        
        halign, valign = self.align
        
        if halign == 'center': x += (width - textwidth)/2
        if halign == 'right': x += (width - textwidth)
        
        if valign == 'center': y += (height - textheight)/2
        if valign == 'bottom': y += (height - textheight)
        
        self.rect = (x, y, textwidth, textheight)        

    def getsizeg(self):
        self.prepare()
        return self.ungrid(*self.textsurface.get_size())
