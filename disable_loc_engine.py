import serial
import time
    
_ser = serial.Serial("/dev/ttyACM0")
_ser.baudrate = 115200
_ser.timeout = 3

_ser.write('reset\r'.encode())
time.sleep(2)
_ser.write('\r\r'.encode())
time.sleep(1)
_ser.reset_input_buffer()
_ser.write('acts 0 0 0 0 0 0 0 2 1\r'.encode())
print(_ser.read_until(b'\n'))
time.sleep(2)
_ser.write('reset\r'.encode())

print("config done")
exit(1)