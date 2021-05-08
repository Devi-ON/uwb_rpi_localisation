from Anchor import *
from trilateration import *

import time
import serial


def write(str):
    ser.write(str.encode())



def loadAnchors():

    # this .txt file contains info about all currently positioned anchors
    # should be downloaded from the server at startup to be stay up to date
    with open("anchor_positions.txt", 'r') as f:
        lineList = f.readlines()

    anchors = []

    for i in range(0, len(lineList)):

        if(lineList[i][0] == '#'): # this is a comment line
            continue
        
        # okunan lineların sonundaki newline characterini al
        lineList[i] = lineList[i].rstrip('\n')
        anchors.append(Anchor(*(lineList[i].split(' '))))

    return anchors

def main():

    # load anchors into memory
    anchors = loadAnchors()
    print("The following anchors are being loaded:\n")
    print(*anchors, sep = '\n') # print anchors

    ser = serial.Serial('com4')
    ser.baudrate = 115200
    # ser.timeout = 1

    # ser.write('reset\r'.encode())
    # print("log: reset issued on uwb module")
    # time.sleep(3)
    # ser.write('\r\r'.encode())
    # time.sleep(1)
    # ser.write('les\r'.encode())
    # time.sleep(1)
    ser.reset_input_buffer()
    print("log: input buffer resetted")

    while True:
        print("new reading")
        read_str = ser.read_until(expected = b'\n', size=None)
        print(read_str)






if __name__ == '__main__':
    main()