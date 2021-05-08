import serial
import time
    
_ser = serial.Serial("/dev/ttyACM0")
_ser.baudrate = 115200
_ser.timeout = 1

_ser.write('reset\r'.encode())
time.sleep(3)
_ser.write('\r\r'.encode())
time.sleep(1)
_ser.write('nmt\r'.encode())
time.sleep(1)
_ser.write('\r\r'.encode())
time.sleep(1)
_ser.write('lep\r'.encode())
time.sleep(1)

print("entering while 1")
while True:
    t = _ser.read_until(b'\n').decode()
    t = t.rstrip("\n")
    t = t.split(",")
    print(*t, sep="   ")