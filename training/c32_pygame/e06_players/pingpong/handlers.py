from game.handlers import EventHandler, KeyHandler

class ChangeStatus(EventHandler):
    def __init__(self, game, done):
        super().__init__(game)
        self.done = done

    def run(self, event):
        self.game.done = self.done

class KeyPrinter(KeyHandler):
    def action(self, key):
        print(key)