from Anchor import *
from trilateration import *

import time
import serial
import sys  # for using CLI arguments

def initDataTransfer(_ser):
    
    _ser.write('reset\r'.encode())
    log("reset issued on uwb module")
    time.sleep(3)
    _ser.write('\r\r'.encode())
    time.sleep(1)
    _ser.write('les\r'.encode())
    time.sleep(1)

def sendPositionToServer(_pos):
    print("POSITON INFO SENT TO SERVER -> ", _pos)


def log(*args):
    #print("log: ", *args)
    pass

# prints members of a list each on a newline
def printListMembers(list):
    for l in list:
        print(l)

def loadAnchors():

    # this .txt file contains info about all currently positioned anchors
    # should be downloaded from the server at startup to be stay up to date
    with open("anchor_positions.txt", 'r') as f:
        lineList = f.readlines()

    anchors = []

    for i in range(0, len(lineList)):

        if(lineList[i][0] == '#'): # this is a comment line
            continue
        
        # strip the newline characters at the end of the read lines
        lineList[i] = lineList[i].rstrip('\n')
        anchors.append(Anchor(*(lineList[i].split(' '))))

    return anchors

# call format is "python tag.py <serial_port>"
def main():

    # load anchors into memory
    anchors = loadAnchors()
    #print("The following anchors are being loaded:\n")
    #print(*anchors, sep = '\n') # print anchors

    # initialize the serial interface
    # print("CLI ARGUMENTS UNPACKED : ", *(sys.argv))
    try:
        ser = serial.Serial(sys.argv[1])    # argv[0] is the filename!
    except IndexError:
        print("The call format is \"python tag.py <serial_port>\"")
        print("aborting.....")
        exit(1)
    
    ser.baudrate = 115200
    ser.timeout = 1

    # the location engine has to be disabled beforehand !

    # init data transfer from UWB to tag
    # initDataTransfer(ser)

    ser.reset_input_buffer()
    #print("log: input buffer resetted")

    ec = 0      # estimation counter
    estimate_cumulative = [0, 0]    # x, y pair

    while True:

        log("new reading")
        read_str = ser.read_until(expected = b'\n', size=None)
        read_str = read_str.rstrip(b' \r\n')
        read_str = read_str.decode()    # convert bytes object to a str object
        distance_readings = read_str.split(sep=' ')
        
        #printListMembers(distance_readings)
        
        anchor_id_dist_pairs = []    # members will be ( , )

        for dr in distance_readings:
            try:
                anchor_id_dist_pairs.append((dr[0:4], float(dr[-4:])))
            except ValueError:
                continue

        anchor_pos_dist = []   # members will be ( , , )
        
        for aidp in anchor_id_dist_pairs:
            
            aID = aidp[0]
            aDist = aidp[1]

            for a in anchors:
                if(a.id == aID):
                    anchor_pos_dist.append((a.x, a.y, aDist))

        #print(anchor_pos_dist)

        args = [arg for subtuple in anchor_pos_dist[0:3] for arg in subtuple]

        if(len(args) != 9):
            log("length of args is not 9, continued loop")
            continue
        else:
            position_estimate = trilateration(*args)
            log("estimation number ", ec)
            #print("Estimated Position : ", position_estimate)
            estimate_cumulative = [x + y for x, y in zip(estimate_cumulative, position_estimate)]
            ec = ec + 1   # increase estimation counter
            
            if (ec == 10):
                ec = 0
                sendPositionToServer([x/10 for x in estimate_cumulative])
                estimate_cumulative = [0, 0]



if __name__ == '__main__':
    main()