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
    def __init__(self, x, y, radius, color):
        self.center = (x, y)
        self.radius = radius
        self.color = color
        self.delta = (1, 1)
