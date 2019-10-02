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
        
    def start(self):
        self.init()
        self.main()
    
    def main(self):
        pg.time.delay(self.delay)
        self.redraw()
    
    def redraw(self):
        pass
