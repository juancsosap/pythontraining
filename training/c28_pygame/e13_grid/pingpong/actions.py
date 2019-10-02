from game.actions import Action

class MoveBall(Action):
    def run(self):
        xg, yg = self.item.centerg
        dx, dy = self.item.delta
        radiusg = self.item.radiusg
        widthg, heightg = self.game.gridshape
        th = self.game.borderg * 2

        if(dx == -1 and xg - radiusg < th): 
            dx = 1
        if(dx == 1 and xg + radiusg > widthg - th): 
            dx = -1

        if(dy == -1 and yg - radiusg < th): 
            dy = 1
        if(dy == 1 and yg + radiusg > heightg - th): 
            dy = -1

        self.item.delta = (dx, dy)
        self.item.centerg = xg + dx, yg + dy

class MoveUp(Action):
    def run(self):
        xg, yg = self.item.xg, self.item.yg
        th = self.game.borderg * 2
        if(yg > th): 
            self.item.yg -= 1

class MoveDown(Action):
    def run(self):
        widthg, heightg = self.game.gridshape
        xg, yg = self.item.xg, self.item.yg
        th = self.game.borderg * 2
        if(yg + self.item.heightg < heightg - th): 
            self.item.yg += 1
