#!/usr/bin/python
#########		
#Wrapper for the Finger Printer sensor and transmission Demo
#########		

#########		
import sys
from sys import argv
import os
import time
import serial
import Adafruit_BBIO.UART as UART
import sensor		#Module that carries out sensoe operations
import data_process	#Module that transforms the fingerprint data to the desired form
#########		

def init(tty):
	tty.write("AT+CMGF=1\r")
	tmp = tty.read(32)
	if "OK" not in tmp:
		if '>' in tmp:
			tty.write('\x1B')
		return False
	print "GSM initiated"
	return True

#########		
#Establish connection in the serial port
#########		

num = "+447923598328"

if '+' in argv[-1]:
	num = argv[-1]

#Create /dev/ttyO4 on the OS

os.environ['LD_LIBRARY_PATH'] = "/root/scannerapi/vendors/les/lib:/root/scannerapi/vendors/les/lib/arm-linux-gnueabihf"

#Setup the serial connection with python

uart = open("/sys/devices/bone_capemgr.9/slots", 'w') 
uart.write("enable-uart5")
uart.close()
UART.setup("UART5")
tty = serial.Serial("/dev/ttyO4", baudrate = 115200, xonxoff = True, timeout = 3)
print "Serial Connection initiated\n"

while not init(tty):
	continue
#Wait for the GSM/Audio module to send the OK signal

#########		
	

#########		
#The main loop
#########		

		
#The sensor reads the finger print in the desired format 
#and store it in a file the name of which is stored
	
print "Getting fingerprint..."
file = sensor.get("LES");
print "Fingerprint received"

#The data is processed


to_send = data_process.data_process(file)

i = 0

while i < len(to_send):
	print i+1
	resend = False
	tty.flush()
	tty.write("AT+CMGS=\""+ num + "\"\r")
	s = ""
	tmpc = tty.read()
	while(tmpc not in ['>', ''] and len(s) <= 50):
		time.sleep(0.01)
		if tmpc not in ['\r', '\n']:
			s += tmpc
		if len(argv) > 1 and 'v' in argv[1]:
			print s
		tmpc = tty.read()
	print s
	tty.write(to_send[i])
        tmps = tty.read(len(to_send[i]) + 1).strip()
	print tmps
	if to_send[i] == tmps:
		time.sleep(0.01)
		while tty.read() != '\x1A':
			time.sleep(0.01)
			tty.write('\x1A')
		tty.flush()
		print "Waiting for Responce"
		tmpc = tty.read()
		s = tmpc
		while "OK" not in s:
			
			if len(argv) > 1 and 'v' in argv[1]:
				print s
			time.sleep(0.01)
			tmpc = tty.read()
			s += tmpc
			if len(argv) > 1 and 'v' in argv[1]:
				print s
			if "ERROR" in s or (len(s) > 25 and tmpc == ''):
				print s
				resend = True
				break
		if not resend:
			print to_send[i] + " OK"
			i += 1
		else:
			print "Error Resend"

	else:
		print [tmps]
		print len(tmps)
		print [to_send[i]]
		print len(to_send[i])
		print "Error! Noise!"
		tty.write('\x1B')
		time.sleep(0.01)
		while tty.read() != '\x1B':
			time.sleep(0.01)
			tty.write('\x1B')
		tty.flush()
