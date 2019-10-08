class EventHandler:
    def __init__(self, game):
        self.game = game
    
    def run(self, event):
        pass

class Nothing(EventHandler):
    pass

class KeyHandler(EventHandler):
    def __init__(self, game, keys):
        super().__init__(game)
        self.keys = keys
    
    def run(self, event):
        if(event.key in self.keys):
            self.action(event.key)
    
    def action(self, key):
        pass

class KeyPlayerHandler(KeyHandler):
    def __init__(self, game, keys, player):
        super().__init__(game, keys)
        self.player = player
