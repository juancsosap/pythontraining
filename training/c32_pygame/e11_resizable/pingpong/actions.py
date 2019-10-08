from game.actions import Action

class MoveBall(Action):
    def run(self):
        x, y = self.item.center
        dx, dy = self.item.delta
        width, height = self.game.size
        radius = self.item.radius
        th = self.game.border * 2

        if(dx == -1 and x - radius < th): dx = 1
        if(dx == 1 and x + radius > width - th): dx = -1

        if(dy == -1 and y -radius < th): dy = 1
        if(dy == 1 and y + radius > height - th): dy = -1

        self.item.delta = (dx, dy)
        self.item.center = (x + self.game.grid * dx, y + self.game.grid * dy)

class MoveUp(Action):
    def run(self):
        x, y = self.item.corner()
        th = self.game.border * 2 + self.game.grid
        if(y >= th): 
            self.item.y -= self.game.grid

class MoveDown(Action):
    def run(self):
        width, height = self.game.size
        x, y = self.item.corner()
        th = self.game.border * 2 + self.game.grid
        if(y + self.item.size <= height - th): 
            self.item.y += self.game.grid
