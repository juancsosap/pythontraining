import pygame as pg
# pip install pygame

from game import GameWindow

class Game:
    def __init__(self, title, size, gridshape=None, fps=30, resizable=False):
        self.title = title
        self.size = size
        self.gridshape = gridshape
        self.fps = fps # Frames per Seconds
        self.resizable = resizable

        self.flag = 'intro'

    def __del__(self):
        pg.quit()

    def init(self):
        pg.init()
        self.clock = pg.time.Clock()

        if(self.resizable): flags = pg.RESIZABLE

        pg.display.set_caption(self.title)

        self.surface = pg.display.set_mode(self.size, flags)        

        self.events = list()
        self.done = False

    def start(self):
        self.init()
        self.main()    

    def main(self):
        self.window = GameWindow(self)
        self.window.start()
    
    def register_event(self, ctype, handler, dtype=None):
        self.events.append((ctype, handler, True))
        if dtype != None: 
            self.events.append((dtype, handler, False))
