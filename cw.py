#!/usr/bin/python 

import serial, readchar, time, os

print "Q exit  . dot  / dah"
print "PTT Z on X off"
ser=serial.Serial()
ser.port="/dev/ttyUSB0" #Set port
ser.open()
ser.setRTS(0) # or ser.setDTR(0)
dottime = (100.0 / 1000.0) #Dot time
freq=500 #500 Hertz tone

def dot():
	ser.setRTS(1)
        #time.sleep (dottime)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( dottime, freq ))
        ser.setRTS(0)
        time.sleep (dottime/2)

def dat():
        ser.setRTS(1)
        #time.sleep (3*dottime)
	os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 3*dottime, freq ))
        ser.setRTS(0)
        time.sleep (dottime/2)

if __name__ == '__main__':
        
        while 1:
                c = readchar.readchar()
		if c == 'Q':     ## Exit
                        break
                if c =='.':
                        print ". ";
                        dot()
                if c =='/':
                        print "_ ";
			dat()

                if c =='a':
                        print "a ";
			dot(); dat();
                if c =='b':
                        print "b ";
			dat(); dot(); dot(); dot();
                if c =='c':
                        print "c ";
			dot(); dat(); dot(); dat();
                if c =='d':
                        print "d ";
			dat(); dot(); dot();
                if c =='e':
                        print "e ";
			dot();
                if c =='f':
                        print "f ";
			dot(); dot(); dat(); dot();
                if c =='g':
                        print "g ";
			dat(); dat(); dot();
                if c =='h':
                        print "h ";
			dot(); dot(); dot(); dot();
                if c =='i':
                        print "i ";
			dot(); dot(); 
                if c =='j':
                        print "j ";
			dot(); dat(); dat(); dat(); 
                if c =='k':
                        print "k ";
			dat(); dot(); dat();
                if c =='l':
                        print "l ";
			dot(); dat(); dot(); dot();  
                if c =='m':
                        print "m ";
			dat(); dat(); 
                if c =='n':
                        print "n ";
			dat(); dot(); 
                if c =='o':
                        print "o ";
			dat(); dat(); dat();
                if c =='p':
                        print "p ";
			dot(); dat(); dat(); dot(); 
                if c =='q':
                        print "q ";
			dat(); dat(); dot(); dat(); 
                if c =='r':
                        print "r ";
			dot(); dat(); dot();
                if c =='s':
                        print "s ";
			dot(); dot(); dot();
                if c =='t':
                        print "t ";
			dat(); 
                if c =='u':
                        print "u ";
			dot(); dot(); dat(); 
                if c =='v':
                        print "v ";
			dot(); dot(); dot(); dat(); 
                if c =='w':
                        print "w ";
			dot(); dat(); dat(); 
                if c =='x':
                        print "x ";
			dat(); dot(); dot(); dat(); 
                if c =='y':
                        print "y ";
			dat(); dot(); dat(); dat(); 
                if c =='z':
                        print "z ";
			dat(); dat(); dot(); dot(); 

                if c >= '0' and c < '6' :
			print c;
                        for x in range(0, int(c)):
				dot(); 
			for x in range(1, 6-int(c)):
				dat();  

                if c > '5' and c <= '9' :
			print c;
                        for x in range(0, int(c)-5):
				dat(); 
			for x in range(0, 10-int(c)):
				dot();  



                if c =='Z':
                        print "PTT ON"
                        ser.setRTS(1)
                if c =='X':
                        print "PTT OFF"
                        ser.setRTS(0)






print "DE SV2RCK 73"
ser.close()
