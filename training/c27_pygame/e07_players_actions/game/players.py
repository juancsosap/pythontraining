from game.items import Item

class Player(Item):
    def __init__(self, x, y):
        self.x, self.y = x, y
