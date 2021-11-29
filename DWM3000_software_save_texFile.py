import serial
import sys
# import threading
import re
import time
import csv
import re
import os

try:
    ser = serial.Serial( port='COM34',
                         baudrate=9600,
                         bytesize=serial.EIGHTBITS,
                         parity=serial.PARITY_NONE,
                         timeout=1 )
    print ("Serial port is open")
    #print (ser.readline())
except Exception as e:
    print ("error open serial port: " + str(e))
    exit()

file = open('Samples.txt', "w")
#saveFile = open(file, 'w')
iteration = 200;
real_distance = 0.50
for i in range(iteration):
    try:
        ser_bytes =str (ser.readline()) # to filter data
        if ser_bytes.find('DIST: ') != -1:
            ruh_data = ser_bytes.split('DIST: ')
            if ruh_data[1].find(' ')!= -1:
                data = ruh_data[1].split(' ')
                float_data = float(data[0])
                print ('distance :', float_data)
                file.write(str(float_data) + "\\\ ") # -- format-- sava Samples in .tex file
                # with open("Bills.txt", "w") as tex_file:
                #     tex_file.write((ser_bytes))
                # # f.close()
                with open("test_data.csv","a") as f:
                    writer = csv.writer(f,delimiter=",")
                    writer.writerow([time.time(),float_data])
    except:
        print("Keyboard Interrupt")
        ser.close()
        f.close()
        file.close()
        # tex_file.close()
        break

ser.close()
f.close()
file.close()
