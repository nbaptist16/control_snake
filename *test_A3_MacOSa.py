# Install the pyautogui and pyserial libraries
import serial
import time
import pyautogui

# Below are the strings used for cursor movements
# taken from the pyautogui reference:
# https://pyautogui.readthedocs.io/en/latest/keyboard.html
#
# For mouse commands use these:
# https://pyautogui.readthedocs.io/en/latest/mouse.html

str_up="up"		
str_down="down"
str_left="left"
str_right="right"

# Make sure the port and baudrate matches that of the Arduino
# Serial.begin(xxxx).
# In Windows you can use the ArduinoIDE Tools>Port menu to get 
# your board's port name and in Mac OS open a Terminal and type:
#      ls /dev/tty.usb* 
ArduinoSerial = serial.Serial(port='/dev/cu.usbmodem1411', baudrate=115200)
time.sleep(2)

while 1:
	incoming = str (ArduinoSerial.read(1)) #Read one byte from serial port
	print(incoming)

	if 'A' in incoming:
		pyautogui.keyDown(str_left)  # Press left and ...
		pyautogui.keyUp(str_left)    # release
	elif 'C' in incoming:
		pyautogui.keyDown(str_right) # Press right and ...
		pyautogui.keyUp(str_right)   # release

	ArduinoSerial.reset_input_buffer()  # Flush the serial port
	
