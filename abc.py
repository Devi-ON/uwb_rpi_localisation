import serial
import time
import csv

fieldnames = ["x_for_plt", "y_for_plt"]
ser = serial.Serial('com3', 115200)





def write(str):
    ser.write(str.encode())

ser.write('reset\r'.encode())
time.sleep(3)
ser.write('\r\r'.encode())
time.sleep(1)
ser.write('lec\r'.encode())
time.sleep(1)
ser.reset_input_buffer()
i = 0
count = 0
sumx = 0
sumy = 0

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while(1):
    
    
        
    txt = ""
    readByte = ser.read(1).decode()
    
    while(readByte != '\r'):
        readByte = ser.read(1).decode()
        txt += readByte
        #print(txt)
        #time.sleep(0.005)
    #print(txt)
    
    list_lec = txt.split(",")
    length_of_list = len(list_lec)
    if(length_of_list>7):
        x1 = float(list_lec[4])
        y1 = float(list_lec[5])
        d1 = float(list_lec[7])
    if(length_of_list>13):
        x2 = float(list_lec[10])
        y2 = float(list_lec[11])
        d2 = float(list_lec[13])
    if(length_of_list>19):
        x3 = float(list_lec[16])
        y3 = float(list_lec[17])
        d3 = float(list_lec[19])

        a1 = 2*(x1-x3);
        a2 = 2*(y1-y3);
        a3 = 2*(x2-x3);
        a4 = 2*(y2-y3);
        b1 = pow(x1,2)-pow(x3,2)+pow(y1,2)-pow(y3,2)+pow(d3,2)-pow(d1,2);
        b2 = pow(x2,2)-pow(x3,2)+pow(y2,2)-pow(y3,2)+pow(d3,2)-pow(d2,2);

        det_ATA = (pow(a1,2)+pow(a3,2))*(pow(a2,2)+pow(a4,2)) - (a1*a2+a3*a4)*(a1*a2+a3*a4);
        estimatedLocation = [0,0]
        estimatedLocation[0] = (1/det_ATA)*((pow(a2,2)+pow(a4,2))*(a1*b1+a3*b2)-(a1*a2+a3*a4)*(a2*b1+a4*b2));
        estimatedLocation[1] = (1/det_ATA)*((pow(a1,2)+pow(a3,2))*(a2*b1+a4*b2)-(a1*a2+a3*a4)*(a1*b1+a3*b2));
        if(count==10):
            print("Estimated Location: x = {:.2f} cm,  y = {:.2f} cm".format(sumx/10,sumy/10))


            with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            x_for_plt = sumx/10
            y_for_plt = sumy/10
            
            info = {
            "x_for_plt": x_for_plt,
            "y_for_plt": y_for_plt
            }
            csv_writer.writerow(info)
            
            count = 0
            sumx = 0
            sumy = 0
        #print(estimatedLocation)
        sumx = sumx + estimatedLocation[0]
        sumy = sumy + estimatedLocation[1]
        count = count+1


