    init data transfer from UWB to tag
    ser.write('reset\r'.encode())
    #print("log: reset issued on uwb module")
    time.sleep(3)
    ser.write('\r\r'.encode())
    time.sleep(1)
    ser.write('les\r'.encode())
    time.sleep(1)