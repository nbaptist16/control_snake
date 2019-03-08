# control_snake
Code for an Arduino-powered controller for the popular game, Slither.io

Download and install Python 3:

https://www.python.org/downloads/

Installation notes:
https://pyautogui.readthedocs.io/en/latest/install.html



In Windows, open a DOS shell (cmd) and install these modules:

c:\Python\scripts\pip.exe install pyautogui
c:\Python\scripts\pip.exe install pyserial


In Mac OS, open a terminal window and do this:

pip3 install pyobjc-core
pip3 install pyobjc
pip3 install pyautogui
pip3 install pyserial



To run the programs:

1) Program an arduino to read a sensor (analog input) and
   print characters to the serial port. The baudrate for the
   serial port, e.g. Serial.begin(115200), will have to match
   the one in the Python script (see below). 


2) Adapt the example Python script to identify the characters
   that the Arduino is writing and produce the desired keystrokes
   in your computer. You need to identify which port the Arduino
   is connected to: in Windows you can use the Arduino 
   IDE Tools>Port menu and in Mac OS open a terminal and type:
   ls /dev/tty.usb* . Replace the port name in the python script
   with your board's address and use the same baudrate as the
   Arduino, e.g.:
 
   ArduinoSerial = serial.Serial(port='/dev/tty.usbserial-A050260JB', baudrate=115200)

	Upload the Arduino script to the board.


3) Run the Python script and leave it running in the background.
   For example, open a DOS shell (cmd), navigate to your Python
   installation directory and run the Python script from there, 
   e.g.
   
       c:\Python\python.exe test_A3.py

   This assumes that you saved the test_A3.py script in the 
   same installation folder. Otherwise, type the path to it, e.g.

       c:\Python\python.exe c:\Python\myDirectory\test_A3.py

   In MacOS use Terminal to navigate to the directory of your Python
   script, then type: python3 test_A3.py (or whatever the script is 
   called) and leave it running. Click on another window or open
   an app and you will control de cursor movement in it. 

4) To be able to control apps in Mac OS, you may need to allow the 
   Terminal to control your computer. Open System Preferences>Security 
   & Privacy and add Terminal to the list of Apps that control the 
   computer.  

This project has many components. Debug one by one until each 
works independently and then try them together.


5) To play, open a window in your browser with the url http://slither.io/.
   Enter a nickname of your choosing and press play.
   Tilt the controller left and right to steer, and press the spacebar for
   a speed boost!

   Eat to grow longer, and try not to run into anyone!
