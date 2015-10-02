#!/usr/bin/python
import Adafruit_BBIO.UART as UART
import serial
UART.setup("UART5")
tty = serial.Serial("/dev/ttyO4", baudrate = 9600, xonxoff = True, timeout = 10)
while(1):
	print tty.read()
