import random
from game.items import Player, Rect, Circle

class Player(Player):
    def __init__(self, game, xg, yg, widthg, heightg, color):
        super().__init__(game, xg, yg)

        self.points = 0
        self.widthg, self.heightg = widthg, heightg
        self.color = color
    
    def draw(self, surface):
        self.prepare()
        Rect(self.game, self.xg, self.yg, self.widthg, self.heightg, self.color).draw(surface)
    
    def resize(self, oldgridshape, newgridshape):
        owidthg, oheightg = oldgridshape
        nwidthg, nheightg = newgridshape
        
        self.xg *= nwidthg / owidthg
        self.yg *= nheightg / oheightg

class Ball(Circle):
    def __init__(self, game, radiusg, color):
        self.game = game
        self.radiusg = radiusg
        self.color = color

        widthg, heightg = self.game.gridshape
        borderg = self.game.borderg
        
        gridy = heightg - borderg * 4
        self.centerg = widthg // 2, self.rand(0, gridy, 1, borderg * 2)
        dx, dy = self.rand(0, 1, 2, -1), self.rand(0, 1, 2, -1)

        self.delta = (dx, dy)
        
    def rand(self, ini, end, mul, offset):
        return random.randint(ini, end) * mul + offset
