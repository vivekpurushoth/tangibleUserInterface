import cv 
import os
import time
import thread
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
yx=-1
yy=-1
bx=-1
by=-1


def yellowAndBlue(img): 
    global yx
    global yy
    global bx
    global by
                
    #blur the source image to reduce color noise 
    cv.Smooth(img, img, cv.CV_BLUR, 3); 
    
    #convert the image to hsv(Hue, Saturation, Value) so its  
    #easier to determine the color to track(hue) 
    hsv_img = cv.CreateImage(cv.GetSize(img), 8, 3) 
    cv.CvtColor(img, hsv_img, cv.CV_BGR2HSV)
    
    #limit all pixels that don't match our criteria, in this case we are  
    #looking for purple but if you want you can adjust the first value in  
    #both turples which is the hue range(120,140).  OpenCV uses 0-180 as  
    #a hue range for the HSV color model 
    thresholded_img =  cv.CreateImage(cv.GetSize(hsv_img), 8, 1) 


    cv.InRangeS(hsv_img, (20, 100, 100), (30, 255, 255), thresholded_img) #yellow

    #determine the objects moments and check that the area is large enough to be our object 
    mat=cv.GetMat(thresholded_img)
    moments = cv.Moments(mat, 0) 
    area = cv.GetCentralMoment(moments, 0, 0) 
    
    #there can be noise in the video so ignore objects with small areas 
    if(area > 100000): 
        #determine the x and y coordinates of the center of the object 
        #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 


        x = cv.GetSpatialMoment(moments, 1, 0)/area 
        y = cv.GetSpatialMoment(moments, 0, 1)/area
        x=int(x)
        y=int(y)
        yx=x
        yy=y
        cv.Circle(img,(x,y),5,(0,0,0),-1)

    cv.InRangeS(hsv_img, (100, 80, 80), (120, 255, 255), thresholded_img) #blue

    #determine the objects moments and check that the area is large enough to be our object 
    mat=cv.GetMat(thresholded_img)
    moments = cv.Moments(mat, 0) 
    area = cv.GetCentralMoment(moments, 0, 0) 
    
    #there can be noise in the video so ignore objects with small areas 
    if(area > 100): 
        #determine the x and y coordinates of the center of the object 
        #we are tracking by dividing the 1, 0 and 0, 1 moments by the area 


        x = cv.GetSpatialMoment(moments, 1, 0)/area 
        y = cv.GetSpatialMoment(moments, 0, 1)/area
        x=int(x)
        y=int(y)
        bx=x
        by=y
        cv.Circle(img,(x,y),5,(0,0,255),-1)

                
if __name__=="__main__": 
    color_tracker_window = "remoteSteering" #Store the name of the window in a string
    cv.NamedWindow( color_tracker_window, 1 ) #Assign the name of the window to the opencv output window
    cap=cv.CaptureFromCAM(1) #Capture from the external webcam and not from the internal webcam of the laptop
    count=1    
    while True:
        img = cv.QueryFrame(cap) #Get one frame of the webcam
        size = cv.GetSize(img) #Get the size of the image
        thumbnail = cv.CreateImage((size[0]/2,size[1]/2),img.depth,img.nChannels) #Create an image that is half the size of the frame image
        cv.Resize(img,thumbnail) #Assign the original frame image to the smaller image just created to enhance the performance
        yellowAndBlue(thumbnail) #Detect colors yellow and blue and update their coordinates in a global variable
        
        if by!=-1 and yy!=-1:
            data="W=1=1"
            client_socket.sendto(data, ("localhost",5001))
        
            if count%1==0:
                if((by-yy)>=40 ):
            
                    data="A=1=1"
                    client_socket.sendto(data, ("localhost",5001))
                    
                    client_socket1.sendto(data, ("localhost",5006))                    
                
                elif ((yy-by)>=40) :
                    
                    data="D=1=1"
                    client_socket.sendto(data, ("localhost",5001))
                    
                    client_socket1.sendto(data, ("localhost",5006))
                    
                    print "right"

                else:
                    data="D=1=1"
                    client_socket1.sendto(data, ("localhost",5006))
                    data="A=1=1"
                    client_socket1.sendto(data, ("localhost",5006))

            count=count+1
        else:
            data="W=1=1"
            client_socket1.sendto(data, ("localhost",5006))
            
            data="A=1=1"
            client_socket1.sendto(data, ("localhost",5006))
           
            data="D=1=1"
            client_socket1.sendto(data, ("localhost",5006))
            
            print "no"


        yx=-1
        yy=-1
        bx=-1
        by=-1

        cv.Flip(img,None, 1);
        cv.ShowImage(color_tracker_window,thumbnail) 

        if cv.WaitKey(10) == 27: #Exit the program if escape key is pressed in the keyboard
            break      