import pygame
import time
import pandas as pd
import csv

ORIGIN = (30, 30)

DI_W = 20
DI_H = 20

WALL_W = 1400
WALL_H = 700

VISITOR_RADIUS = DI_W/2

RATIO = 2

RGB_WHITE = (255, 255, 255)
RGB_CYAN = (0, 255, 255)
RGB_BLACK = (0, 0, 0,)
RGB_BLUE = (0, 0, 255)
RGB_GREEN = (0, 255, 0)
RGB_GRAY = (220, 220, 220)

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

d_name_rgb = {
    "red" : (255, 0, 0),
    "green" : (0, 255, 0),
    "blue" : (0, 0, 255),
    "yellow" : (255, 255, 0),
    "orange" : (228, 113, 25)
}

class Visitor():
    def __init__(self):
        self.x = 0  # real location w.r.t origin, cm
        self.y = 0
        self.center = (0, 0)    # pixel, w.r.t pygame origin at top left
        pass

    def draw(self, surface):
        self.center = (ORIGIN[0] + RATIO*self.x), (ORIGIN[1] + RATIO*self.y)
        pygame.draw.circle(surface, RGB_CYAN , self.center, VISITOR_RADIUS)

    def writePos(self, surface):
        text1 = font.render("{}, {}".format(visitor.x, visitor.y), True, RGB_BLACK)
        text1Rect = text1.get_rect()
        text1Pos = visitor.center[0] - text1Rect.width/2, visitor.center[1] - text1Rect.height/2 - 10
        museumWindow.blit(text1, text1Pos)



class DisplayItem():
    def __init__(self, _x, _y, _colorRGB):
        self.x = _x
        self.y = _y
        self.colorRGB = _colorRGB

    def draw(self, surface):
        diRect = pygame.Rect(0, 0, DI_W, DI_H)
        diRect.center = (ORIGIN[0] + RATIO*self.x), (ORIGIN[1] + RATIO*self.y)
        pygame.draw.rect(surface, self.colorRGB, diRect, 0) 

def drawOrigin(surface):
    pygame.draw.circle(surface, RGB_BLACK, ORIGIN, 8)

def drawWalls(surface):
    wallRect = pygame.Rect(*ORIGIN, WALL_W, WALL_H)
    pygame.draw.rect(surface, RGB_BLUE, wallRect, 1)

def loadDisplayItems():

    displayItems = []   # to be returned
    
    # this .txt file contains info about all currently positioned anchors
    # should be downloaded from the server at startup to be stay up to date
    with open("anchor_positions.txt", 'r') as f:
        lineList = f.readlines()

    for i in range(0, len(lineList)):

        if(lineList[i][0] == '#'): # this is a comment line
            continue
        
        # strip the newline characters at the end of the read lines
        lineList[i] = lineList[i].rstrip('\n')
        line = lineList[i].split(' ')
        displayItems.append(DisplayItem(
            int(100*float(line[2])),
            int(100*float(line[3])),
            d_name_rgb[line[0]]
        ))

    return displayItems

## main code ##
pygame.init()
museumWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

visitor = Visitor()
font = pygame.font.Font(None, 18)

dispItems = loadDisplayItems()

runFlag = True


while runFlag:

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            runFlag = False

    museumWindow.fill(RGB_GRAY)
    drawWalls(museumWindow)
    drawOrigin(museumWindow)

    for di in dispItems:
        di.draw(museumWindow)

    data = pd.read_csv('data.csv')
    x_pd = data['x_cm']
    y_pd = data['y_cm']
    visitor.x = int((x_pd.values[len(x_pd.values) - 1]))
    visitor.y = int((y_pd.values[len(y_pd.values) - 1]))

    visitor.draw(museumWindow)
    visitor.writePos(museumWindow)
    
    pygame.display.update()
    time.sleep(0.2) 
    
