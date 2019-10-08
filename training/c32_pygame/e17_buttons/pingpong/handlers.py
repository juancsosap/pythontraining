from game.handlers import *
from pingpong import actions

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

class ResizeMainWindow(ResizeWindowHandler):
    def action(self, start=True):
        if(self.game.factor):
            oldgridshape = self.game.gridshape
            width, height = self.oldsize
            self.game.gridshape = round(width / 5), round(height / 5)
            self.game.window.player1.resize(oldgridshape, self.game.gridshape)
            self.game.window.player2.resize(oldgridshape, self.game.gridshape)

class ResizeInfoWindow(ResizeWindowHandler):
    def action(self, start=True):
        self.game.window.initialdraw()
