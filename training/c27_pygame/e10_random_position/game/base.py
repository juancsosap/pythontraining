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

        self.surface = pg.display.set_mode(self.size)        
        self.done = False
        self.events = list()
        self.actions = list()
    
    def start(self):
        self.init()
        self.main()    

    def main(self):
        while not self.done:
            pg.time.delay(self.delay)
            self.validate_events()
            self.run_actions()
            self.redraw()
            pg.display.update()

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
