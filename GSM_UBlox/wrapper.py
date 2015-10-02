#!/usr/bin/python
#########		
#Wrapper for the Finger Printer sensor and transmission Demo
#########		

#########		
import sys
import os
import time
import serial
import Adafruit_BBIO.UART as UART
from cStringIO import StringIO
import sensor		#Module that carries out sensoe operations
import data_process	#Module that transforms the fingerprint data to the desired form
import data_transmit	#Module that transmit the data as specified
#########		

def send(s):
	print s.strip('\n')
	for i in s:
		tty.write(i)
		time.sleep(0.008)
	tty.write(' ')
	time.sleep(0.008)
	verify = tty.read(len(s) + 1)
	print verify
	if verify == s.strip('\n'):
		tty.write('T')
		time.sleep(0.02)
		while tty.read()!='o':
			continue
		print "New SMS"
		return True
	else: 
		tty.write('F')
		time.sleep(0.02)
		while tty.read()!='o':
			continue
		return False
		
#########		
#Verify if the options are valid
#########		

if len(sys.argv) < 3 :
	print "Please specify the method and file form\n"
	print "Method: "
	for i in data_transmit.method:
		print i
	print "Form: "
	for i in data_process.form:
		print i
	sys.exit()

method = sys.argv[1];
form = sys.argv[2];

if method not in data_transmit.method:
	print "First option must be in:"
	for i in data_transmit.method:
		print i
	form = "-template"
	sys.exit()

if method in data_transmit.simple:
	print "Second option is ignored for this transmission method\n"

elif form not in data_process.form:
	print "Second option must be in:"
	for i in data_process.form:
		print i
	sys.exit()	
#########		

#########		
#Establish connection in the serial port
#########		


#Create /dev/ttyO4 on the OS

os.environ['LD_LIBRARY_PATH'] = "/root/scannerapi/vendors/les/lib:/root/scannerapi/vendors/les/lib/arm-linux-gnueabihf"

#Setup the serial connection with python

uart = open("/sys/devices/bone_capemgr.9/slots", 'w') 
uart.write("enable-uart5")
uart.close()
UART.setup("UART5")
tty = serial.Serial("/dev/ttyO4", baudrate = 9600, xonxoff = True, timeout = 3)
print "Serial Connection initiated\n"

#Wait for the GSM/Audio module to send the OK signal

while tty.read() != 'o':
	print "Waiting for sender device to be ready..."
tty.write('S')
#########		

#########		
#The main loop
#########		

#Use try-except to capture and terminate on 'Ctrl-C' signal

try:
	while True:
		
		#The sensor reads the finger print in the desired format 
		#and store it in a file the name of which is stored
		
		print "Getting fingerprint..."
		file = sensor.get(form);
		print "Fingerprint received"

		#The data is processed according to the format

		to_send = data_process.data_process(file, form, method)
		to_send = to_send.split(' ')
		for i in to_send:
			while (not send(i)):
				continue

		#Send the data

#		data_transmit.send(tty, to_send, form)


		break
		
except KeyboardInterrupt:
	pass
