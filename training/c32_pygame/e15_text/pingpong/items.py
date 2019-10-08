import random
from game.items import Player, Rect, Circle

class Player(Player):
    def __init__(self, game, xg, yg, widthg, heightg, color):
        super().__init__(game, xg, yg, widthg, heightg)
        self.color = color
        self.points = 0
    
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
        self.reset(game)
        super().__init__(game, self.xg, self.yg, radiusg, color)
        
    def rand(self, ini, end, mul, offset):
        return random.randint(ini, end) * mul + offset
    
    def reset(self, game):
        widthg, heightg = game.gridshape
        borderg = game.borderg
        
        gridy = heightg - borderg * 5 - game.playerheightg
        self.xg, self.yg = widthg // 2, self.rand(0, gridy, 1, borderg * 3 + game.playerheightg)
        self.centerg = self.xg, self.yg
        
        dx, dy = self.rand(0, 1, 2, -1), self.rand(0, 1, 2, -1)
        self.delta = (dx, dy)
