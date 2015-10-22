#!/usr/bin/python 

import serial, readchar, time, os

print "q exit  . dot  / dah"
print "PTT z on x off"
ser=serial.Serial()
ser.port="/dev/ttyUSB0" #Set port
ser.open()
ser.setRTS(1) # or ser.setDTR(0)

if __name__ == '__main__':
        dot = (100.0 / 1000.0) #Dot time
        while 1:
                c = readchar.readkey()
                if c == 'q':     ## Exit
                        break
                if c =='.':
                        print ". ";
                        ser.setRTS(0)
                        #time.sleep (dot)
                        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( dot, 500 ))
                        ser.setRTS(1)
                        time.sleep (dot/2)
                if c =='/':
                        print "_ ";
                        ser.setRTS(0)
                        #time.sleep (3*dot)
                        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 3*dot, 500 ))
                        ser.setRTS(1)
                        time.sleep (dot/2)
                if c =='z':
                        print "PTT ON"
                        ser.setRTS(0)
                if c =='x':
                        print "PTT OFF"
                        ser.setRTS(1)

ser.close()
print "73"
