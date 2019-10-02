import pygame as pg
# pip install pygame

class GameWindow:
    def __init__(self, game):
        self.game = game

    def init(self):
        self.surface = self.game.surface
        self.done = False
        self.events = list()
        self.actions = list()
    
    def start(self):
        self.init()
        self.main()    

    def main(self):
        self.done = False
        self.initialdraw()
        while not self.done:
            self.validate_events()
            self.run_actions()
            self.redraw()
            pg.display.update()
            self.game.clock.tick(self.game.fps)

    def initialdraw(self):
        pass

    def redraw(self):
        pass

    def register_event(self, ctype, handler, dtype=None):
        self.events.append((ctype, handler, True))
        if dtype != None: 
            self.events.append((dtype, handler, False))

    def validate_events(self):
        for event in pg.event.get():
            events = self.events + self.game.events
            for type, handler, start in events:
                if event.type == type:
                    handler.run(event, start)

    def register_actions(self, action):
        self.actions.append(action)
    
    def unregister_actions(self, action):
        self.actions.remove(action)

    def run_actions(self):
        for action in self.actions:
            action.run()
