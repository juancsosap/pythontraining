import pygame as pg
# pip install pygame

class Item:
    def draw(self, surface):
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

class Colors:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)
    AQUA = (0, 255, 255)
    WHITE = (255, 255, 255)