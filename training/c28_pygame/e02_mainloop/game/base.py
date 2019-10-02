import pygame as pg
# pip install pygame

class Game:
    def __init__(self, title, size, delay=100):
        self.size = size
        self.delay = delay
        self.title = title

    def __del__(self):
        pg.quit()

    def init(self):
        pg.init()
        pg.display.set_caption(self.title)
        pg.display.set_mode(self.size)
        
        self.done = False

    def start(self):
        self.init()
        self.main()    
        
    def main(self):
        while not self.done:
            pg.time.delay(self.delay)
            self.redraw()
            self.done = True

    def redraw(self):
        pass
