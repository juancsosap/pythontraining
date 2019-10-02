import pygame as pg
from game import Game, handlers as gh

from pingpong import MainWindow, IntroWindow, PauseWindow

class PingPong(Game):
    def __init__(self, fps=30, factor=True):
        super().__init__('Ping Pong', (500, 300), (100, 60), fps=fps, resizable=True)
        self.factor = factor
        self.start()

    def init(self):
        super().init()

        self.borderg = 1

        self.register()
        
    def register(self):
        self.register_event(pg.QUIT, gh.Done(self, 'exit'))
        
    def main(self):
        while not self.done:
            if self.flag == 'intro':
                self.window = IntroWindow(self)
                self.window.start()

            if self.flag == 'start':
                self.mainwindow = MainWindow(self)
                self.window = self.mainwindow
                self.window.start()
            elif self.flag == 'continue':
                self.window = self.mainwindow
                self.window.main()

            if self.flag == 'pause':
                self.window = PauseWindow(self)
                self.window.start()
            
            if self.flag == 'exit':
                self.done = True
        