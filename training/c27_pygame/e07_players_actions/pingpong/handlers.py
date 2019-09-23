from game.handlers import *

class ChangeStatus(EventHandler):
    def __init__(self, game, done):
        super().__init__(game)
        self.done = done

    def run(self, event):
        self.game.done = self.done

class KeyPrinter(KeyHandler):
    def action(self, key):
        print(key)

class MoveUp(KeyPlayerHandler):
    def action(self, key):
        x, y = self.player.corner()
        th = self.game.border * 2 + self.game.grid
        if(y >= th): self.player.y -= self.game.grid

class MoveDown(KeyPlayerHandler):
    def action(self, key):
        width, height = self.game.size
        x, y = self.player.corner()
        th = self.game.border * 2 + self.game.grid
        if(y + self.player.size <= height - th): self.player.y += self.game.grid
