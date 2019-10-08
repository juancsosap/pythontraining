class Action:
    def __init__(self, game, item):
        self.game = game
        self.item = item

    def run(self):
        pass

class Done(Action):
    def run(self):
        self.game.flag = self.flag
        self.game.window.done = True
