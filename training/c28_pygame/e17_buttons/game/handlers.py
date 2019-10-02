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
            self.game.window.register_actions(self.actionobj)
        else:
            self.game.window.unregister_actions(self.actionobj)

class ResizeWindowHandler(EventHandler):
    def run(self, event, start=True):
        self.oldsize = self.game.size
        self.game.size = (event.w, event.h)
        self.game.surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
        self.game.window.surface = self.game.surface
        self.action(start)
    
    def action(self, start=True):
        pass

class Done(EventHandler):
    def __init__(self, game, flag):
        super().__init__(game)
        self.flag = flag
    
    def run(self, event, start=True):
        self.game.flag = self.flag
        self.game.window.done = True

class KeyDone(KeyHandler):
    def __init__(self, game, keys, flag):
        super().__init__(game, keys)
        self.flag = flag
        
    def action(self, key, start=True):
        self.game.flag = self.flag
        self.game.window.done = True

class ControlHandler(EventHandler):
    def __init__(self, game, control, states):
        super().__init__(game)
        self.control = control
        self.states = states
    
    def run(self, event, start=True):
        pass

class ControlMouseOverHandler(ControlHandler):
    def __init__(self, game, control, states):
        super().__init__(game, control, states)
    
    def run(self, event, start=True):
        if(self.control.iswithin(event.pos)):
            self.control.state = self.states[self.control.state]
        else:
            self.control.state = 'normal'
        self.control.draw(self.game.window.surface)
        pg.display.update()
    
class ControlMouseButtonHandler(ControlHandler):
    def __init__(self, game, control, button, states):
        super().__init__(game, control, states)
        self.button = button
    
    def run(self, event, start=True):
        if(self.control.iswithin(event.pos)):
            if(event.button == self.button):
                self.control.state = self.states[self.control.state]
        else:
            self.control.state = 'normal'
        self.control.draw(self.game.window.surface)
        pg.display.update()
