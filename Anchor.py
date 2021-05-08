class Anchor:
    def __init__(self, _color = "", _id = "", _xPos = 0, _yPos = 0):
        self.x = float(_xPos)
        self.y = float(_yPos)
        self.color = _color
        self.id = _id

    def __str__(self):
        return "x(m): " + str(self.x) + ", y(m): " + str(self.y) + ", color: " + self.color + ", id: " + self.id
