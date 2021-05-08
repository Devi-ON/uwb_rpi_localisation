d_IDtoColor = {

	"green" : "20C6",
    "yellow" : "089E",
	"red" : "2A6D",
	"orange" : "2BC4",
}

class Anchor:
    def __init__(self, _xPos = 0, _yPos = 0, _color = "", _id = ""):
        self.xPos = _xPos
        self.yPos = _yPos
        self.color = _color
        self.id = _id

    def __str__(self):
        return "x: " + str(self.xPos) + ", y: " + str(self.yPos) + ", color: " + self.color + ", id: " + self.id

class Tag:
    def __init__(self)



anchorYellow = Anchor(-1, -1, "yellow", d_IDtoColor["yellow"])
anchorGreen = Anchor(-1, -1, "green", d_IDtoColor["green"])
anchorOrange = Anchor(-1, -1, "orange", d_IDtoColor["orange"])
anchorRed = Anchor(-1, -1, "red", d_IDtoColor["red"])

anchorList = [anchorYellow, anchorRed, anchorOrange]

print("those anchors are defined:")
for a in anchorList:
    print(a)


# for a in anchorList:
#     if("red" == a.color):
#         print(a.xPos)

# print("hi", anchorRed.color)