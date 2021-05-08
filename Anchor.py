class Anchor:
    def __init__(self, _color = "", _id = "", _xPos = 0, _yPos = 0):
        self.xPos = float(_xPos)
        self.yPos = float(_yPos)
        self.color = _color
        self.id = _id

    def __str__(self):
        return "x(m): " + str(self.xPos) + ", y(m): " + str(self.yPos) + ", color: " + self.color + ", id: " + self.id
