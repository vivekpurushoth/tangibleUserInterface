# UDP server example
import socket
import string
import time
import uinput
import os

#Creating a socket object of address family AF_INET and type datagram.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Bind the socket to the port 5001
server_socket.bind(("", 5001))


print"UDPServer Waiting for client on port 5001"

def emitCharacter(character):
	global device
	global dictionaryEvents
	device.emit(dictionaryEvents[character],1)
	device.emit(dictionaryEvents[character],0)


def initialize():
	global events
	global device
	global dictionaryEvents
	events = (
    uinput.REL_X,
    uinput.REL_Y,
    uinput.BTN_LEFT,
    uinput.BTN_RIGHT,uinput.KEY_A,uinput.KEY_B,uinput.KEY_C,uinput.KEY_D,uinput.KEY_E,uinput.KEY_F,uinput.KEY_G,uinput.KEY_H,uinput.KEY_I,uinput.KEY_J,uinput.KEY_K,uinput.KEY_L,uinput.KEY_M,uinput.KEY_N,uinput.KEY_O,uinput.KEY_P,uinput.KEY_Q,uinput.KEY_R,uinput.KEY_S,uinput.KEY_T,uinput.KEY_U,uinput.KEY_V,uinput.KEY_W, uinput.KEY_X, uinput.KEY_Y, uinput.KEY_Z,uinput.KEY_OPEN, uinput.KEY_ESC,
 uinput.KEY_1,
 uinput.KEY_2,
 uinput.KEY_3 ,
 uinput.KEY_4 ,
 uinput.KEY_5 ,
 uinput.KEY_6,
 uinput.KEY_7 ,
 uinput.KEY_8,
 uinput.KEY_9 ,
 uinput.KEY_0 ,
 uinput.KEY_MINUS,
 uinput.KEY_EQUAL,
 uinput.KEY_BACKSPACE,
 uinput.KEY_TAB,
 uinput.KEY_LEFTBRACE ,
 uinput.KEY_RIGHTBRACE,
 uinput.KEY_ENTER,
 uinput.KEY_LEFTCTRL,
 uinput.KEY_COMMA,
 uinput.KEY_DOT,
 uinput.KEY_SLASH,
 uinput.KEY_RIGHTSHIFT,
 uinput.KEY_KPASTERISK,
 uinput.KEY_LEFTALT,
 uinput.KEY_SPACE,
 uinput.KEY_CAPSLOCK,
 uinput.KEY_F1,
 uinput.KEY_F2,
 uinput.KEY_F3,
 uinput.KEY_F4,
 uinput.KEY_F5,
 uinput.KEY_F7,
 uinput.KEY_F8,
 uinput.KEY_F9,
 uinput.KEY_F10,
 uinput.KEY_NUMLOCK,
 uinput.KEY_SCROLLLOCK,
 uinput.KEY_KP7,
 uinput.KEY_KP8,
 uinput.KEY_KP9,
 uinput.KEY_KPMINUS,
 uinput.KEY_KP4,
 uinput.KEY_KP5,
 uinput.KEY_KP6,
 uinput.KEY_KPPLUS,
 uinput.KEY_KP1,
 uinput.KEY_KP2,
 uinput.KEY_KP3,
 uinput.KEY_KP0,
 uinput.KEY_KPDOT,
 uinput.KEY_102ND,
 uinput.KEY_F11,
 uinput.KEY_F12,
 uinput.KEY_KPJPCOMMA,
 uinput.KEY_KPENTER,
 uinput.KEY_RIGHTCTRL,
 uinput.KEY_KPSLASH ,
 uinput.KEY_SYSRQ ,
 uinput.KEY_RIGHTALT ,
 uinput.KEY_LINEFEED ,
 uinput.KEY_HOME ,
 uinput.KEY_UP ,
 uinput.KEY_PAGEUP ,
 uinput.KEY_LEFT ,
 uinput.KEY_RIGHT ,
 uinput.KEY_END ,
 uinput.KEY_DOWN ,
 uinput.KEY_PAGEDOWN ,
 uinput.KEY_INSERT ,
 uinput.KEY_DELETE ,
 uinput.KEY_MACRO ,
 uinput.KEY_MUTE ,
 uinput.KEY_VOLUMEDOWN ,
 uinput.KEY_VOLUMEUP ,
 uinput.KEY_POWER ,
 uinput.KEY_KPEQUAL ,
 uinput.KEY_KPPLUSMINUS ,
 uinput.KEY_PAUSE ,
 uinput.KEY_SCALE ,
 uinput.KEY_KPCOMMA ,
 uinput.KEY_HANGEUL ,
 uinput.KEY_HANJA ,
 uinput.KEY_YEN ,
 uinput.KEY_LEFTMETA ,
 uinput.KEY_RIGHTMETA ,
 uinput.KEY_COMPOSE ,
 uinput.KEY_STOP ,
 uinput.KEY_AGAIN ,
 uinput.KEY_PROPS ,
 uinput.KEY_UNDO ,
 uinput.KEY_FRONT ,
 uinput.KEY_COPY ,
 uinput.KEY_OPEN ,
 uinput.KEY_PASTE ,
 uinput.KEY_FIND ,
 uinput.KEY_CUT ,
 uinput.KEY_HELP ,
 uinput.KEY_MENU ,
 uinput.KEY_CALC ,
 uinput.KEY_SETUP,
 uinput.BTN_LEFT,
 uinput.BTN_RIGHT,
 uinput.ABS_X ,
 uinput.ABS_Y,
 uinput.KEY_SEMICOLON,
)
	device = uinput.Device(events)
	dictionaryEvents = {}
	dictionaryEvents['A'] = uinput.KEY_A
	dictionaryEvents['B'] = uinput.KEY_B
	dictionaryEvents['C'] = uinput.KEY_C
	dictionaryEvents['D'] = uinput.KEY_D
	dictionaryEvents['E'] = uinput.KEY_E
	dictionaryEvents['F'] = uinput.KEY_F
	dictionaryEvents['G'] = uinput.KEY_G
	dictionaryEvents['H'] = uinput.KEY_H
	dictionaryEvents['I'] = uinput.KEY_I
	dictionaryEvents['J'] = uinput.KEY_J
	dictionaryEvents['K'] = uinput.KEY_K
	dictionaryEvents['L'] = uinput.KEY_L
	dictionaryEvents['M'] = uinput.KEY_M
	dictionaryEvents['N'] = uinput.KEY_N
	dictionaryEvents['O'] = uinput.KEY_O
	dictionaryEvents['P'] = uinput.KEY_P
	dictionaryEvents['Q'] = uinput.KEY_Q
	dictionaryEvents['R'] = uinput.KEY_R
	dictionaryEvents['S'] = uinput.KEY_S
	dictionaryEvents['T'] = uinput.KEY_T
	dictionaryEvents['U'] = uinput.KEY_U
	dictionaryEvents['V'] = uinput.KEY_V
	dictionaryEvents['W'] = uinput.KEY_W
	dictionaryEvents['X'] = uinput.KEY_X
	dictionaryEvents['Y'] = uinput.KEY_Y
	dictionaryEvents['Z'] = uinput.KEY_Z
	dictionaryEvents['1'] = uinput.KEY_1
	dictionaryEvents['2'] = uinput.KEY_2
	dictionaryEvents['3'] = uinput.KEY_3
	dictionaryEvents['4'] = uinput.KEY_4
	dictionaryEvents['5'] = uinput.KEY_5
	dictionaryEvents['6'] = uinput.KEY_6
	dictionaryEvents['7'] = uinput.KEY_7
	dictionaryEvents['8'] = uinput.KEY_8
	dictionaryEvents['9'] = uinput.KEY_9
	dictionaryEvents['0'] = uinput.KEY_0
	dictionaryEvents['MINUS'] = uinput.KEY_MINUS
	dictionaryEvents['EQUAL'] = uinput.KEY_EQUAL
	dictionaryEvents['BACKSPACE'] = uinput.KEY_BACKSPACE
	dictionaryEvents['TAB'] = uinput.KEY_TAB
	dictionaryEvents['LEFTBRACE'] = uinput.KEY_LEFTBRACE
	dictionaryEvents['RIGHTBRACE'] = uinput.KEY_RIGHTBRACE
	dictionaryEvents['ENTER'] = uinput.KEY_ENTER
	dictionaryEvents['COMMA'] = uinput.KEY_COMMA
	dictionaryEvents['SLASH'] = uinput.KEY_SLASH
	dictionaryEvents['RIGHTSHIFT'] = uinput.KEY_RIGHTSHIFT
	dictionaryEvents['LEFTALT'] = uinput.KEY_LEFTALT
	dictionaryEvents['SPACE'] = uinput.KEY_SPACE
	dictionaryEvents['CAPSLOCK'] = uinput.KEY_CAPSLOCK
	dictionaryEvents['LEFTCTRL'] = uinput.KEY_LEFTCTRL
	dictionaryEvents['LEFTMETA'] = uinput.KEY_LEFTMETA
	dictionaryEvents['RIGHTALT'] = uinput.KEY_RIGHTALT
	dictionaryEvents['RIGHTCTRL'] = uinput.KEY_RIGHTCTRL
	dictionaryEvents['LEFT'] = uinput.KEY_LEFT
	dictionaryEvents['DOWN'] = uinput.KEY_DOWN
	dictionaryEvents['RIGHT'] = uinput.KEY_RIGHT
	dictionaryEvents['DOT'] = uinput.KEY_DOT
	dictionaryEvents['DEL'] = uinput.KEY_DELETE
	dictionaryEvents['UP'] = uinput.KEY_UP
	dictionaryEvents['F1'] = uinput.KEY_F1
	dictionaryEvents['F2'] = uinput.KEY_F2
	dictionaryEvents['F3'] = uinput.KEY_F3
	dictionaryEvents['F4'] = uinput.KEY_F4
	dictionaryEvents['F5'] = uinput.KEY_F5
	dictionaryEvents['F6'] = uinput.KEY_F6
	dictionaryEvents['F7'] = uinput.KEY_F7
	dictionaryEvents['F8'] = uinput.KEY_F8
	dictionaryEvents['F9'] = uinput.KEY_F9
	dictionaryEvents['F10'] = uinput.KEY_F10
	dictionaryEvents['F11'] = uinput.KEY_F11
	dictionaryEvents['F12'] = uinput.KEY_F12
	dictionaryEvents['ESC'] = uinput.KEY_ESC
	dictionaryEvents['SEMI'] = uinput.KEY_SEMICOLON
	dictionaryEvents['ENTER'] = uinput.KEY_ENTER
    


def sense():
	while True:
		#Collect the data obtained from the udp client. Setting the maximum buffer size as 256
		data, address = server_socket.recvfrom(256)
		#Interpreting the data obtained from the client
		data=string.split(data,"=")
		if data[0]=="M": #mouse move event
			print data[1]
			print data[2]
			device.emit(uinput.REL_X, int(data[1]), syn=False)
			device.emit(uinput.REL_Y, int(data[2]))
		elif data[0]=="C": #mouse left click event
			print "clicked"
			device.emit(uinput.BTN_LEFT,1)
			device.emit(uinput.BTN_LEFT,0)
		elif data[0]=="R": #mouse right click event
			print "Right click"
			device.emit(uinput.BTN_RIGHT,1)
			device.emit(uinput.BTN_RIGHT,0)
		elif data[0]=="K": #keyboard keypress event
			if data[1]==str(1): #Comparing if the parameter is string 1
				if data[2]==" ":
					emitCharacter("SPACE") #Emitting space
				elif data[2]=="\n":
					emitCharacter("ENTER") #Emitting enter
				else:
					emitCharacter(data[2]) #Emitting normal characters
			else:
				os.system("xdotool key BackSpace") #Generating backspace by using xdoltool

'''
The main function, the first function that will be called
'''
def main():
	initialize() #Initialize all the global variables necessary
	sense() #Start detecting the different events obtained to the server
#End of main

'''
The starting point of the entire program
'''
if __name__ == "__main__":
	main()