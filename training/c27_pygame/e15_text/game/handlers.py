import pygame as pg

class EventHandler:
    def __init__(self, game):
        self.game = game
    
    def run(self, event, start=True):
        pass

class Nothing(EventHandler):
    pass

class KeyHandler(EventHandler):
    def __init__(self, game, keys):
        super().__init__(game)
        self.keys = keys
    
    def run(self, event, start=True):
        if(event.key in self.keys):
            self.action(event.key, start)
    
    def action(self, key, start=True):
        pass

class KeyPlayerHandler(KeyHandler):
    def __init__(self, game, keys, player):
        super().__init__(game, keys)
        self.player = player

class KeyActionHandler(KeyHandler):
    def __init__(self, game, keys, item, actiontype):
        super().__init__(game, keys)
        self.item = item
        self.actionobj = actiontype(game, item)

    def action(self, key, start=True):
        if(start):
            self.game.register_actions(self.actionobj)
        else:
            self.game.unregister_actions(self.actionobj)

class ResizeWindowHandler(EventHandler):
    def run(self, event, start=True):
        self.game.size = (event.w, event.h)
        self.action(start)
        self.game.surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
    
    def action(self, start=True):
        pass
