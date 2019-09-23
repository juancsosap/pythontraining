import pygame as pg
# pip install pygame

class Item:
    def draw(self, surface):
        pass

    def resize(self):
        pass

class Rect(Item):
    def __init__(self, x, y, width, height, color):
        self.rect = (x, y, width, height)
        self.color = color

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect)

class Ellipse(Rect):
    def draw(self, surface):
        pg.draw.ellipse(surface, self.color, self.rect)

class Circle(Item):
    def __init__(self, x, y, radius, color):
        self.center = (x, y)
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pg.draw.circle(surface, self.color, self.center, self.radius)

class Line(Item):
    def __init__(self, x_ini, y_ini, x_end, y_end, width, color):
        self.ini = (x_ini, y_ini)
        self.end = (x_end, y_end)
        self.width = width
        self.color = color

    def draw(self, surface):
        pg.draw.line(surface, self.color, self.ini, self.end, self.width)

class Player(Item):
    def __init__(self, game, id):
        self.game, self.id = game, id
