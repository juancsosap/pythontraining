import random
from game.items import Player, Rect, Circle

class Player(Player):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.points = 0
        self.size = 50
        self.width = 10
        self.color = color
    
    def corner(self):
        x = self.x - self.width // 2
        y = self.y - self.size // 2
        return (x, y)

    def draw(self, surface):
        x, y = self.corner()
        Rect(x, y, self.width, self.size, self.color).draw(surface)

class Ball(Circle):
    def __init__(self, size, grid, border, radius, color):
        width, height = size
        
        gridy = (height - border * 4) / grid
        x, y = int(width / 2), self.rand(0, gridy, grid, border * 2)
        dx, dy = self.rand(0, 1, 2, -1), self.rand(0, 1, 2, -1)

        self.center = (x, y)
        self.radius = radius
        self.color = color
        self.delta = (dx, dy)

    def rand(self, ini, end, mul, offset):
        return random.randint(ini, end) * mul + offset