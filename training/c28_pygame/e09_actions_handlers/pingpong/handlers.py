from game.handlers import *
from pingpong import actions

class ChangeStatus(EventHandler):
    def __init__(self, game, done):
        super().__init__(game)
        self.done = done

    def run(self, event, start=True):
        self.game.done = self.done

class KeyPrinter(KeyHandler):
    def action(self, key, start=True):
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
