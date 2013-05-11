#!/usr/bin/python

import cwiid #Library to interact with wii remote
import math #Library to perform mathematic operations like sqrt, pow
from time import sleep #Library that helps us to introduce delay
import uinput #To emit keyboard characters, mouse click and movement
import os  #Required to run xdotool commands
from Xlib import X, display #To interact with x11 server

'''
This function takes a character and generates an interrupt(event) to the kernel.
'''  
def emitCharacter(character):
	if (character == 'APOS'):
		os.system("xdotool key apostrophe ")
	else:	
		device.emit(dictionaryEvents[character],1)
		device.emit(dictionaryEvents[character],0)
#End of emitCharacter

'''
This function sets up all the global variables that will be later used by other modules of the program
'''
def setup():
	global w
	global d
	global s
	global root
	
	print 'Put Wiimote in discoverable mode now (press 1+2)...' #Prompt the user to put the wiimote in bluetooth discoverable mode
	w = cwiid.Wiimote() #get the reference of the wiimote
	w.rpt_mode = cwiid.RPT_IR #request nunchuk to be active.
	w.led = 1 #turn on one LED light in wiimote to indicate that the bluetooth connection is successful
	d = display.Display()
	s = d.screen()
	root = s.root
#End of setup

#initializing variables that will be later used as reference
def initialize():

	global keyescX
	global keyescY
	global keytabX
	global keytabY
	global keycapsX
	global keycapsY
	global keylshiftX
	global keylshiftY
	global keyspcX
	global keyspcY
	global keyctrlX
	global keyctrlY
	global capsLockPressed

	global mousex
	global mousey
	global mousexb
	global mouseyb
	global mousexd
	global mouseyd

	global events
	global dictionaryEvents
	
	#Keyboard related initialization
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

	#Mouse related initialization
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
#End of initialize


'''
This function is used to help the user calibrate the keyboard layout.
'''
def calibrate():
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
#End of calibrate

'''
This function performs the actual sensing of the keyboard and mouse events.
It also emits the interrupt to the system
'''
def sense():
	print "Sensing begins"
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
#End of sense


'''
The main function, the first function that will be called
'''
def main():
	setup() #Connect the wiimote to the computer via bluetooth, get the reference of the object, 	
	initialize() #Initialize all the global variables necessary
	calibrate() #Calibrate the keyboard layout by prompting the user to press the 5 predefined keys
	sense() #Start sensing every IR led light that appers in the frame of wiiremote, map the coordinates and generate the event.
#End of main

'''
The starting point of the entire program
'''
if __name__ == "__main__":
	main()
