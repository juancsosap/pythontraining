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
        xg, yg = self.player.xg, self.player.yg
        th = self.game.borderg * 2
        if(yg >= th): self.player.yg -= 1

class MoveDown(KeyPlayerHandler):
    def action(self, key):
        widthg, heightg = self.game.gridshape
        xg, yg = self.player.xg, self.player.yg
        th = self.game.borderg * 2
        if(yg + self.player.heightg <= heightg - th): self.player.yg += 1

class ResizeWindow(ResizeWindowHandler):
    def action(self, start=True):
        if(self.game.factor):
            oldgridshape = self.game.gridshape
            width, height = self.game.size
            self.game.gridshape = round(width / 5), round(height / 5)
            self.game.player1.resize(oldgridshape, self.game.gridshape)
            self.game.player2.resize(oldgridshape, self.game.gridshape)
        
