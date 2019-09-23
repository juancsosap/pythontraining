import pygame as pg
# pip install pygame

class Game:
    def __init__(self, title, size, gridshape=None, fps=30, resizable=False):
        self.title = title
        self.size = size
        self.gridshape = gridshape
        self.fps = fps # Frames per Seconds
        self.resizable = resizable

    def __del__(self):
        pg.quit()

    def init(self):
        pg.init()
        self.clock = pg.time.Clock()

        if(self.resizable): flags = pg.RESIZABLE

        pg.display.set_caption(self.title)

        self.surface = pg.display.set_mode(self.size, flags)        
        self.done = False
        self.events = list()
        self.actions = list()
    
    def start(self):
        self.init()
        self.main()    

    def main(self):
        while not self.done:
            self.validate_events()
            self.run_actions()
            self.redraw()
            pg.display.update()
            self.clock.tick(self.fps)

    def redraw(self):
        pass

    def register_event(self, ctype, handler, dtype=None):
        self.events.append((ctype, handler, True))
        if dtype != None: 
            self.events.append((dtype, handler, False))

    def validate_events(self):
        for event in pg.event.get():
            for type, handler, start in self.events:
                if event.type == type:
                    handler.run(event, start)

    def register_actions(self, action):
        self.actions.append(action)
    
    def unregister_actions(self, action):
        self.actions.remove(action)

    def run_actions(self):
        for action in self.actions:
            action.run()
