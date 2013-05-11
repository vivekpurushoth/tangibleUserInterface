#!/usr/bin/python


import cwiid #Library to interact with wii remote
import math #Library to perform mathematic operations like sqrt, pow
from time import sleep #Library that helps us to introduce delay
import uinput #To emit keyboard characters, mouse click and movement
import os  #Required to run xdotool commands
from Xlib import X, display #To interact with x11 server


#Connect to the wii remote
print 'Put Wiimote in discoverable mode now (press 1+2)...'
w = cwiid.Wiimote()
# Request nunchuk to be active.
w.rpt_mode = cwiid.RPT_IR
# Turn on one LED light in wiimote to indicate that the bluetooth connection is successful
w.led = 1

#initializing variables used in keyboard detection
keytabX = 0 #variable to store Q's initial X
keytabY = 0 #variable to store Q's initial Y
keycapsX = 0 #variable to store A's initial X
keycapsY = 0 #variable to store A's initial Y
keylshiftX = 0 #variable to store Z's initial X
keylshiftY = 0 #variable to store Z's initial Y
keyspcX=0 #variable to store '`' initial X
keyspcY=0 #variable to store '`' initial Y
keyescX=0  #variable to store ESC initial X
keyescY=0  #variable to store ESC initial Y
keyctrlX=0 #variable to store ctrl initial X
keyctrlY=0 #variable to store ctrl initial Y
capsLockPressed = 0 #0-lowercase, 1-uppercase

#Keyboard layout converted into rows of arrays
#escRow = ["ESC","","","F1","F2","F3","F4","","F5","F6","F7","F8","","F9","F10","F11","F12"]
spcRow = ["1","2","3","4","5","6","7","8","9","0","MINUS","EQUAL","SLASH","BACKSPACE"]
tabRow = ["W","E","R","T","Y","U","I","O","P","LEFTBRACE","RIGHTBRACE","ENTER","ENTER","ENTER"]
capsRow = ["S","D","F","G","H","J","K","L","SEMI","APOS"]
lshiftRow = ["Z","X","C","V","B","N","M","COMMA","DOT","SLASH"]
#ctrlRow = ["LEFTCTRL","","LEFTMETA","LEFTALT","SPACE","SPACE","SPACE","SPACE","SPACE","RIGHTALT","RIGHTCTRL","LEFT","DOWN","RIGHT"]
ctrlRow = ["LEFTMETA","LEFT","DOWN","RIGHT"]


#Set the context
d = display.Display()
s = d.screen()
root = s.root  

#three basic co-ordinates to know the position of keyboard layout
#first_cord=[None,None]
#sec_cord=[None,None]
#third_cord=[None,None]  

mousex=0; #current-X
mousey=0; #current-Y
mousexb=0; #backup-X
mouseyb=0; #backup-Y
mousexd=0; #difference-X
mouseyd=0; #difference-Y


#Code to create events for each button pressed
events = (uinput.KEY_A,uinput.KEY_B,uinput.KEY_C,uinput.KEY_D,uinput.KEY_E,uinput.KEY_F,uinput.KEY_G,uinput.KEY_H,uinput.KEY_I,uinput.KEY_J,uinput.KEY_K,uinput.KEY_L,uinput.KEY_M,uinput.KEY_N,uinput.KEY_O,uinput.KEY_P,uinput.KEY_Q,uinput.KEY_R,uinput.KEY_S,uinput.KEY_T,uinput.KEY_U,uinput.KEY_V,uinput.KEY_W, uinput.KEY_X, uinput.KEY_Y, uinput.KEY_Z,uinput.KEY_OPEN, uinput.KEY_ESC,
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
device = uinput.Device(events)  #device initialization for keyboard using uinput
#count=0

def emitCharacter(character):
	if (character == ''):
		return
	if (character == 'A'):
		device.emit(uinput.KEY_A, 1)
		device.emit(uinput.KEY_A, 0)
	if (character == 'B'):
		device.emit(uinput.KEY_B, 1)
		device.emit(uinput.KEY_B, 0)
	if (character == 'C'):
		device.emit(uinput.KEY_C, 1)
		device.emit(uinput.KEY_C, 0)
	if (character == 'D'):
		device.emit(uinput.KEY_D, 1)
		device.emit(uinput.KEY_D, 0)
	if (character == 'E'):
		device.emit(uinput.KEY_E, 1)
		device.emit(uinput.KEY_E, 0)
	if (character == 'F'):
		device.emit(uinput.KEY_F, 1)
		device.emit(uinput.KEY_F, 0)
	if (character == 'G'):
		device.emit(uinput.KEY_G, 1)
		device.emit(uinput.KEY_G, 0)
	if (character == 'H'):
		device.emit(uinput.KEY_H, 1)
		device.emit(uinput.KEY_H, 0)
	if (character == 'I'):
		device.emit(uinput.KEY_I, 1)
		device.emit(uinput.KEY_I, 0)
	if (character == 'J'):
		device.emit(uinput.KEY_J, 1)
		device.emit(uinput.KEY_J, 0)
	if (character == 'K'):
		device.emit(uinput.KEY_K, 1)
		device.emit(uinput.KEY_K, 0)
	if (character == 'L'):
		device.emit(uinput.KEY_L, 1)
		device.emit(uinput.KEY_L, 0)
	if (character == 'M'):
		device.emit(uinput.KEY_M, 1)
		device.emit(uinput.KEY_M, 0)
	if (character == 'N'):
		device.emit(uinput.KEY_N, 1)
		device.emit(uinput.KEY_N, 0)
	if (character == 'O'):
		device.emit(uinput.KEY_O, 1)
		device.emit(uinput.KEY_O, 0)
	if (character == 'P'):
		device.emit(uinput.KEY_P, 1)
		device.emit(uinput.KEY_P, 0)
	if (character == 'Q'):
		device.emit(uinput.KEY_Q, 1)
		device.emit(uinput.KEY_Q, 0)
	if (character == 'R'):
		device.emit(uinput.KEY_R, 1)
		device.emit(uinput.KEY_R, 0)
	if (character == 'S'):
		device.emit(uinput.KEY_S, 1)
		device.emit(uinput.KEY_S, 0)
	if (character == 'T'):
		device.emit(uinput.KEY_T, 1)
		device.emit(uinput.KEY_T, 0)
	if (character == 'U'):
		device.emit(uinput.KEY_U, 1)
		device.emit(uinput.KEY_U, 0)
	if (character == 'V'):
		device.emit(uinput.KEY_V, 1)
		device.emit(uinput.KEY_V, 0)
	if (character == 'W'):
		device.emit(uinput.KEY_W, 1)
		device.emit(uinput.KEY_W, 0)
	if (character == 'X'):
		device.emit(uinput.KEY_X, 1)
		device.emit(uinput.KEY_X, 0)
	if (character == 'Y'):
		device.emit(uinput.KEY_Y, 1)
		device.emit(uinput.KEY_Y, 0)
	if (character == 'Z'):
		device.emit(uinput.KEY_Z, 1)
		device.emit(uinput.KEY_Z, 0)
	if character == '1':
		device.emit(uinput.KEY_1, 1) 
		device.emit(uinput.KEY_1, 0)
	if character == '2':
	     device.emit(uinput.KEY_2, 1) 
	     device.emit(uinput.KEY_2, 0)
	if character == '3':
	     device.emit(uinput.KEY_3, 1) 
	     device.emit(uinput.KEY_3, 0)
	if character == '4':
	     device.emit(uinput.KEY_4, 1) 
	     device.emit(uinput.KEY_4, 0)
	if character == '5':
	     device.emit(uinput.KEY_5, 1) 
	     device.emit(uinput.KEY_5, 0)
	if character == '6':
	     device.emit(uinput.KEY_6, 1) 
	     device.emit(uinput.KEY_6, 0)
	if character == '7':
	     device.emit(uinput.KEY_7, 1) 
	     device.emit(uinput.KEY_7, 0)
	if character == '8':
	     device.emit(uinput.KEY_8, 1) 
	     device.emit(uinput.KEY_8, 0)
	if character == '9':
	     device.emit(uinput.KEY_9, 1) 
	     device.emit(uinput.KEY_9, 0)
	if character == '0':
	     device.emit(uinput.KEY_0, 1) 
	     device.emit(uinput.KEY_0, 0) 
	if character == 'MINUS':
	     device.emit(uinput.KEY_MINUS, 1) 
	     device.emit(uinput.KEY_MINUS, 0)     
	if character == 'EQUAL':
	     device.emit(uinput.KEY_EQUAL, 1) 
	     device.emit(uinput.KEY_EQUAL, 0)
	if character == 'BACKSPACE':
	     device.emit(uinput.KEY_BACKSPACE, 1) 
	     device.emit(uinput.KEY_BACKSPACE, 0)
	if character == 'TAB':
	     device.emit(uinput.KEY_TAB, 1) 
	     device.emit(uinput.KEY_TAB, 0)
	if character == 'LEFTBRACE':
	     device.emit(uinput.KEY_LEFTBRACE, 1) 
	     device.emit(uinput.KEY_LEFTBRACE, 0)    
	if character == 'RIGHTBRACE':
	     device.emit(uinput.KEY_RIGHTBRACE, 1) 
	     device.emit(uinput.KEY_RIGHTBRACE, 0)
	if character == 'ENTER':
	     device.emit(uinput.KEY_ENTER, 1) 
	     device.emit(uinput.KEY_ENTER, 0)     
	if character == 'COMMA':
	     device.emit(uinput.KEY_COMMA, 1) 
	     device.emit(uinput.KEY_COMMA, 0)  
	if character == 'SLASH':
	     device.emit(uinput.KEY_SLASH, 1) 
	     device.emit(uinput.KEY_SLASH, 0)
	if character == 'RIGHTSHIFT':
	     device.emit(uinput.KEY_RIGHTSHIFT, 1) 
	     device.emit(uinput.KEY_RIGHTSHIFT, 0)
	if character == 'LEFTALT':
	     device.emit(uinput.KEY_LEFTALT, 1) 
	     device.emit(uinput.KEY_LEFTALT, 0)
	if character == 'SPACE':
	     device.emit(uinput.KEY_SPACE, 1) 
	     device.emit(uinput.KEY_SPACE, 0)
	if character == 'CAPSLOCK':
	     device.emit(uinput.KEY_CAPSLOCK, 1) 
	     device.emit(uinput.KEY_CAPSLOCK, 0)
	if character == 'LEFTCTRL':
	     device.emit(uinput.KEY_LEFTCTRL, 1)
	     device.emit(uinput.KEY_LEFTCTRL,0)
	     print "ctrl clicked" 
	     #device.emit(uinput.KEY_LEFTCTRL, 0)
	     '''c=get_additional_key()
	     if c == 'V':
	     	os.system("xdotool key Ctrl+V")'''	     
	     sleep(0.1)	    
	if character == 'LEFTMETA':
	     device.emit(uinput.KEY_LEFTMETA, 1) 
	     device.emit(uinput.KEY_LEFTMETA, 0)  
	if character == 'RIGHTALT':
	     device.emit(uinput.KEY_RIGHTALT, 1) 
	     device.emit(uinput.KEY_RIGHTALT, 0) 
	if character == 'RIGHTCTRL':
	     device.emit(uinput.KEY_RIGHTCTRL, 1) 
	     device.emit(uinput.KEY_RIGHTCTRL, 0) 
	if character == 'LEFT':		
	     device.emit(uinput.KEY_LEFT, 1)
	     print "left arrow" 
	     device.emit(uinput.KEY_LEFT, 0)
	if character == 'DOWN':
	     #sleep(1)
	     device.emit(uinput.KEY_DOWN, 1)
	     print "DOWN arrow" 
	     device.emit(uinput.KEY_DOWN, 0) 
	if character == 'RIGHT':
	     device.emit(uinput.KEY_RIGHT, 1)
	     print "right arrow" 
	     device.emit(uinput.KEY_RIGHT, 0) 
	if character == 'DOT':
		 device.emit(uinput.KEY_DOT,1)
		 device.emit(uinput.KEY_DOT,0)
	if character == 'DEL':
		 device.emit(uinput.KEY_DELETE,1)
		 device.emit(uinput.KEY_DELETE,0)
	if (character == 'UP'):
		device.emit(uinput.KEY_UP, 1)
		device.emit(uinput.KEY_UP, 0)
	if  (character == 'F1'):
		device.emit(uinput.KEY_F1, 1)
		device.emit(uinput.KEY_F1, 0)
	if  (character == 'F2'):
		device.emit(uinput.KEY_F2, 1)
		device.emit(uinput.KEY_F2, 0)
	if  (character == 'F3'):
		device.emit(uinput.KEY_F3, 1)
		device.emit(uinput.KEY_F3, 0)
	if  (character == 'F4'):
		device.emit(uinput.KEY_F4, 1)
		device.emit(uinput.KEY_F4, 0)
	if  (character == 'F5'):
		device.emit(uinput.KEY_F5, 1)
		device.emit(uinput.KEY_F5, 0)
	if  (character == 'F6'):
		device.emit(uinput.KEY_F6, 1)
		device.emit(uinput.KEY_F6, 0)
	if  (character == 'F7'):
		device.emit(uinput.KEY_F7, 1)
		device.emit(uinput.KEY_F7, 0)
	if  (character == 'F8'):
		device.emit(uinput.KEY_F8, 1)
		device.emit(uinput.KEY_F8, 0)
	if  (character == 'F9'):
		device.emit(uinput.KEY_F9, 1)
		device.emit(uinput.KEY_F9, 0)
	if  (character == 'F10'):
		device.emit(uinput.KEY_F10, 1)
		device.emit(uinput.KEY_F10, 0)
	if  (character == 'F11'):
		device.emit(uinput.KEY_F11, 1)
		device.emit(uinput.KEY_F11, 0)
	if  (character == 'F12'):
		device.emit(uinput.KEY_F12, 1)
		device.emit(uinput.KEY_F12, 0)
	if  (character == 'ESC'):
		device.emit(uinput.KEY_ESC, 1)
		device.emit(uinput.KEY_ESC, 0)
	if  (character == 'SEMI'):
		device.emit(uinput.KEY_SEMICOLON, 1)
		device.emit(uinput.KEY_SEMICOLON, 0)
	if  (character == 'APOS'):
		os.system("xdotool key apostrophe ")
	if  (character == 'ENTER'):
		device.emit(uinput.KEY_ENTER, 1)
		device.emit(uinput.KEY_ENTER, 0)

#End of code to create events for each button pressed


#code begins here
#positionthekeyboard()

print "press ESC"

while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed esc"
		keyescX = w.state['ir_src'][0]['pos'][0]
		keyescY = w.state['ir_src'][0]['pos'][1]
		print keyescX
		print keyescY
		#w.state['ir_src'][1] = None
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)

sleep(1)



print "press '`' key"

while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed ` key"
		keyspcX = w.state['ir_src'][0]['pos'][0]
		keyspcY = w.state['ir_src'][0]['pos'][1]
		print keyspcX
		print keyspcY
		#w.state['ir_src'][1] = None
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)

sleep(1)



print "press TAB"

while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed TAB"
		keytabX = w.state['ir_src'][0]['pos'][0]
		keytabY = w.state['ir_src'][0]['pos'][1]
		print keytabX
		print keytabY
		#w.state['ir_src'][1] = None
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)

sleep(1)

print "press CAPSLOCK"

while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed CAPSLOCK"
		keycapsX = w.state['ir_src'][0]['pos'][0]
		keycapsY = w.state['ir_src'][0]['pos'][1]
		print keycapsX
		print keycapsY
		#w.state['ir_src'][1] = None
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)


sleep(1)

#print "press Z"
print "press left shift"
while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed left shift"
		keylshiftX = w.state['ir_src'][0]['pos'][0]
		keylshiftY = w.state['ir_src'][0]['pos'][1]
		print keylshiftX
		print keylshiftY
		#w.state['ir_src'][1] = None
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)

sleep(1)

print "press CTRL"

while( 1 ):
	#print w.state['ir_src'][0]
	a = w.state['ir_src'][0]
	if a != None:
		print "pressed CTRL"
		keyctrlX = w.state['ir_src'][0]['pos'][0]
		keyctrlY = w.state['ir_src'][0]['pos'][1]
		print keyctrlX
		print keyctrlY
		w.rpt_mode = cwiid.RPT_IR
		break
	sleep(0.2)

sleep(1)


print "Sensing Starts"
while( 1 ):
	a = w.state['ir_src'][0]
	if a != None:
		print "sensing:"
		try:
			pressedX = w.state['ir_src'][0]['pos'][0]
			pressedY = w.state['ir_src'][0]['pos'][1]
			print pressedX
		except:
			sleep(0.2)
			#a=None#none has been assigned to a
			continue#pass has been converted to continue
		#print pressedX
		#print pressedY
		if(pressedY >= keyescY+80  and pressedX<(keyescX-(14*45))):
			mousexd=mousex-mousexb
			mouseyd=mousey-mouseyb
			data = display.Display().screen().root.query_pointer()._data
			xp = data["root_x"]
			yp = data["root_y"]
			if(mousexd>10 or mousexd<-10 or mouseyd>10 or mouseyd<-10):	
				pass
			else:
				device.emit(uinput.ABS_X,xp+(mousexd*-3),syn=False)
				device.emit(uinput.ABS_Y,yp+(mouseyd*3))
		
				
			mousexb=mousex
			mouseyb=mousey
		
			mousex = pressedX
			mousey = pressedY
			print 'pressed cords:%u %u'%(mousex,mousey)
			print 'mouse cords:%u %u'%(mousex,mousey)
			print 'mouse b cords:%u %u'%(mousexb,mouseyb)
		elif(((pressedY>keyescY-15)and(pressedY<keyescY+15))):
			print "pressedX is %u" %(pressedX)
			print "pressedY is %u" %(pressedY)
			diff = keyescX - pressedX
			print 'diff is %u' %(diff)
			if (diff>=(-20) and diff<=20 ):
				emitCharacter("ESC")
				print "esc pressed"
			if (diff>=61 and diff<103):
				emitCharacter("F1")
				print "F1 pressed"
			if (diff>=104 and diff<=144):
				emitCharacter("F2")
				print "F2 pressed"
			if (diff>=145 and diff<=178):
				emitCharacter("F3")
				print "F3 pressed"
			if (diff>=188 and diff<=231):
				emitCharacter("F4")
				print "F4 pressed"
			if (diff>=253 and diff<=297):
				emitCharacter("F5")
				print "F5 pressed"
			if (diff>=301 and diff<=336):
				emitCharacter("F6")
				print "F6 pressed"
			if (diff>=339 and diff<=376):
				emitCharacter("F7")
				print "F7 pressed"
			if (diff>=379 and diff<=422):
				emitCharacter("F8")
				print "F8 pressed"
			if (diff>=446 and diff<=487):
				emitCharacter("F9")
				print "F9 pressed"
			if (diff>=487 and diff<=527):
				emitCharacter("F10")
				print "F10 pressed"
			if (diff>=527 and diff<=571):
				emitCharacter("F11")
				print "F11 pressed"
			if (diff>=572 and diff<=611):
				emitCharacter("F12")
				print "F12 pressed"
			sleep(0.2)
		elif(((pressedY>keyspcY-15)and(pressedY<keyspcY+15))):
			print "grave row"
			print "pressedX is %u" %(pressedX)
			print "pressedY is %u" %(pressedY)
			diff = keyspcX - pressedX
			if (diff>(-15) and diff<15 ):
				os.system("xdotool key grave")
				print "` pressed"
			elif (diff>656 and diff<686+5 ):
				device.emit(uinput.BTN_LEFT, 1)
				print "left click pressed"
				device.emit(uinput.BTN_LEFT, 0)
			elif (diff>696 and diff<728+5 ):
				device.emit(uinput.BTN_RIGHT, 1)
				print "right click pressed"
				device.emit(uinput.BTN_RIGHT, 0)
			else:
				diff = abs((keyspcX-7)- pressedX) #15
				index = int(((diff)/45.0))
				print 'diffspc is %u' %(diff)
				print 'indexspc is %u' %(index)
				try:
					print spcRow[index]
					emitCharacter(spcRow[index])
				except:
					continue
			sleep(0.2)
		elif(((pressedY>keytabY-15)and(pressedY<keytabY+15))):
			print "tabRow "
			print "pressedX is %u" %(pressedX)
			print "pressedY is %u" %(pressedY)
			diff = keytabX - pressedX
			if (diff>(-15) and diff<15 ):
				emitCharacter("TAB")
				print "tab pressed"
			elif (diff>53 and diff<85):
				emitCharacter("Q")
				print "Q pressed"
			elif (diff>568 and diff<497):
				emitCharacter("ENTER")
				print "enter pressed"
			else:
				diff = ((keytabX-85)- pressedX)
				index = int(round((diff)/45.0))
				print 'difftab is %u' %(diff)
				print 'indextab is %u' %(index)
				try:
					print tabRow[index]
					emitCharacter(tabRow[index])
				except:
					continue
			sleep(0.2)
		elif(((pressedY>keycapsY-15)and(pressedY<keycapsY+15))):
			print "CAPSLOCK Row"
			print "pressedX is %u" %(pressedX)
			print "pressedY is %u" %(pressedY)
			diff = keycapsX - pressedX
			if (diff>(-15) and diff<15 ):
				if(capsLockPressed==0):
					device.emit(uinput.KEY_CAPSLOCK, 1)
					capsLockPressed=1
					print "capslock pressed"
				else:
					device.emit(uinput.KEY_CAPSLOCK, 0)
					capsLockPressed=0
					print "capslock released"				
			elif (diff>62 and diff<94):
				emitCharacter("A")
				print "A pressed"
			elif (diff>518 and diff<547):
				pass
			elif (diff>552-11 and diff<582+5):
				emitCharacter("ENTER")
			else:
				diff= abs((keycapsX-94)- pressedX)
				index = int(round((diff)/45.0))
				print 'diff is %u' %(diff)
				print 'index is %u' %(index)
				try:
					print capsRow[index]
					emitCharacter(capsRow[index])
				except:
					continue
			sleep(0.2)
		elif(((pressedY>keylshiftY-15)and(pressedY<keylshiftY+15))):
			print "left shift row "
			print "pressedX is %u" %(pressedX)
			print "pressedY is %u" %(pressedY)
			diff = keylshiftX - pressedX
			if (diff>(-15) and diff<15 ):
				emitCharacter("RIGHTSHIFT")
				print "rightshift pressed"
			elif(diff>71 and diff<101):
				emitCharacter("Z")
				print "Z pressed"
			elif(diff>516-25 and diff<555-10):
				print "up pressed"
				emitCharacter("UP")
			else:
				diff= abs((keylshiftX-101+10)- pressedX)#101
				index = int(round((diff)/40.0))
				print 'diff is %u' %(diff)
				print 'index is %u' %(index)
				try:
					print lshiftRow[index]
					emitCharacter(lshiftRow[index])
				except:
					continue
			sleep(0.2)
		else:
			if(((pressedY>keyctrlY-20)and(pressedY<keyctrlY+20))):
				print "ctrl row"
				print "pressedX is %u" %(pressedX)
				print "pressedY is %u" %(pressedY)
				diff = keyctrlX - pressedX
				if (diff>(-15) and diff<15 ):
					emitCharacter("LEFTCTRL")
					print "leftctrl pressed"
				elif(diff>52 and diff<77):
					emitCharacter("LEFTMETA")
					print "leftmeta pressed"
				elif(diff>89 and diff<114):
					emitCharacter("LEFTALT")
					print "leftalt pressed"				
				elif(diff>147 and diff<357):
					emitCharacter("SPACE")
					print "space pressed"
				elif(diff>384-65 and diff<355):
					emitCharacter("LEFTALT")
					print "leftalt pressed"
				else:
					diff= abs((keyctrlX-395)- pressedX)
					index = int(((diff)/45.0))
					print 'diff is %u' %(diff)
					print 'index is %u' %(index)
					try:
						print ctrlRow[index]
						emitCharacter(ctrlRow[index])
					except:
						continue
				sleep(0.2)
