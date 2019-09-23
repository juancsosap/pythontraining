import random
from game.items import Player, Rect, Circle

class Player(Player):
    def __init__(self, game, id, color):
        super().__init__(game, id)

        self.points = 0
        self.size = 50
        self.width = 10
        self.color = color

        self.resize()
    
    def corner(self):
        x = self.x - self.width // 2
        y = self.y - self.size // 2
        return (x, y)

    def draw(self, surface):
        x, y = self.corner()
        Rect(x, y, self.width, self.size, self.color).draw(surface)

    def resize(self):
        gwidth, gheight = self.game.size
        space = self.game.border * 2 + self.width 
        self.x = space if self.id == 1 else gwidth - space
        self.y = gheight / 2

class Ball(Circle):
    def __init__(self, game, radius, color):
        self.game = game
        self.radius = radius
        self.color = color
        
        self.resize()

    def rand(self, ini, end, mul, offset):
        return random.randint(round(ini), round(end)) * mul + offset

    def resize(self):
        width, height = self.game.size
        border, grid = self.game.border, self.game.grid
        
        gridy = (height - border * 4) / grid
        x, y = int(width / 2), self.rand(0, gridy, grid, border * 2)
        dx, dy = self.rand(0, 1, 2, -1), self.rand(0, 1, 2, -1)

        self.center = (x, y)
        self.delta = (dx, dy)
