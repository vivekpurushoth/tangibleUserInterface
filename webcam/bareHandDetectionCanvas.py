import numpy as np
import cv2
import cv
import time
import math as em
import time
a=[];
count=0
gmax=[]
thumb=[]
COLOR=[]
#camera is a reference to your actual camera
# -> 0 - internal camera 
# -> 1 - external camera
camera = cv2.VideoCapture(1)
ptsAry=[]
colAry=[]
RED=[0,0,255]
GREEN=[0,255,0]
BLUE=[255,0,0]
WHITE=[255,255,255]
color=WHITE

while True:
    f,im = camera.read() # f - true if next frame was captured correctly, im - the frame captured if success otherwise null
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) #the frame is converted to gray scale frame
    ret,thresh = cv2.threshold(imgray,70,255,cv2.THRESH_BINARY_INV) # ret - true if it was successfully able to convert to black and white, thresh - the converted black and white image
    cv2.imshow("img",thresh) 
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE) #contours - gives the boundary of the image, hierarchy - not using in our code, ignore
    maxAreaElement=0 #The element that holds the current maximum area element in the frame of the webcam
    indexMaxAreaElement=-1 #The index of the maximum area element
    cv2.rectangle(im,(220,20),(260,60),RED,-2) #An option to change color | RED
    cv2.rectangle(im,(280,20),(320,60),GREEN,-2) #An option to change color | GREEN
    cv2.rectangle(im,(340,20),(380,60),BLUE,-2) #An option to change color | BLUE

    #The following code is needed to keep track of your hand movements and redraw on each frame
    for i in range(len(thumb)):
        ele=thumb[i]
        c=COLOR[i]
        for i in range(len(ele)-1):
                cv2.line(im,ele[i],ele[i+1],c[i],10)


    #Obtain the index of the hand contour if it exists
    for i in range(len(contours)):      
        if maxAreaElement<cv2.contourArea(contours[i]):
            maxAreaElement=cv2.contourArea(contours[i])
            indexMaxAreaElement=i
    
    #If the necessary countour was fetched
    if indexMaxAreaElement>-1:
        try:
            cnt = contours[indexMaxAreaElement] #fetch the countour of the hand

            hull = cv2.convexHull(cnt,returnPoints = False) #from the contour fetch the convexHull of the hand (only indicies, use original contour to fetch the actual points)

            count =0 #Re-initialize the count to 0 for each frame to fetch the points for the five fingers
            defects = cv2.convexityDefects(cnt,hull) #defects are the places where the maxima and minima have occured
            prevS = None
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                cv2.line(im,start,end,[0,255,0],2)#code to draw the green line from every start to its corressponding end
                gmax.append(end) #Collecting all the ends in one frame into gmax
            
            #Find the top most defectual point and the left most defectual point and use them as the reference for drawing on the canvas    
            yCurrentMax=480 #480
            ind=-1 #To keep the index of the element which is top most
            lmin=640 # 640
            iterator=-1 #To keep track of the index of the element which is left most
            for i in range(len(gmax)):
                if yCurrentMax>gmax[i][1] : #If the given point lies much farther above the current maxTop presenet
                    ind=i
                    yCurrentMax=gmax[i][1]
                if lmin>gmax[i][0] : #If the given point lies much farther towards the left than the minLeft present 
                    iterator=i
                    lmin=gmax[i][0]
                
            cv2.line(im,gmax[ind],gmax[ind],color,15)
            
            x=gmax[ind][0] #Collect the x coordinates of your hand in this frame
            y=gmax[ind][1] #Collect the y coordinates of your hand in this frame

            if x>=220 and x <=260 and y>=20 and y<=60: #The user intends to select the color RED as his drawing color
                color=RED
            elif x>=280 and x <=320 and y>=20 and y<=60: #The user intends to select the color GREEN as his drawing color
                color=GREEN
            elif x>=340 and x <=380 and y>=20 and y<=60: #The user intends to select the color BLUE as his drawing color
                color=BLUE


            for i in range(len(ptsAry)-1):
                cv2.line(im,ptsAry[i],ptsAry[i+1],colAry[i],10)
            
            
            if gmax[ind][0]-gmax[iterator][0] >60: #If the gesture for drawing is made | The distance between top most and left most is more than a threshold
                ptsAry.append(gmax[ind])
                colAry.append(color)
            else:
                thumb.append(ptsAry)
                COLOR.append(colAry)
                ptsAry=[]
                colAry=[]

            gmax=[]
        except Exception, f:
            print f;
            pass
    else: #The condition when the user has removed his hand from the frame at which the canvas should be cleared
        thumb=[]
        COLOR=[]
        ptsAry=[]
        colAry=[]

    
    cv2.imshow("myImage",im) #Display the output image onto the screen
    if cv.WaitKey(10) == 27: #Press escape to exit the code
        break