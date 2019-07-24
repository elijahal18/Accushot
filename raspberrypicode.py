import pushbuttoncode.py
import imageprocessing.py
import piezo.ino
import datetime
import dataprocessing.py
from picamera import PiCamera
#import all libraries
push=pushbuttoncode()

with picamera.PiCamera() as camera and picamera.PiCamera() as camera1:#use sensors to start and stop cams
    if push==F:
        startTime=imageprocessing.StopWatch.start()
        camera.start_recording('sidevid.h264')
        camera1.start_recording('frontvid.h264')
    
    if piezo()==1:
        endTime=imageprocessing.StopWatch.stop()
        camera.stop_recording()
        camera1.stop_recording()

#use image processing functions to calculate list of coordinates
coor_lst_side=imageprocessing.imageprocessing('sidevid.h264')
coor_lst_front=imageprocessing.imageprocessing('frontvid.h264')
#use data processing functions to find usefull data for user
horizontal_vel=dataprocessing.horizontal_vel(coor_lst_side, startTime,endTime)

vert_vel= dataprocessing.vert_vel(coor_lst_side, startTime,endTime)

projected_dist=dataprocessing.projected_dist(coor_lst_side, startTime, endTime)

target_loc=imageprocessing.target_location('frontvid.h264')

accu=dataprocessing.accu(coor_lst_front, target_loc)

avg=dataprocessing.write_to(accu)
#return values
print("Great shot! Your shot had a horizontal velocity of:",str(horizontal_vel),"A vertical velocity of:",
      str(vert_vel),"Would have gone this far:",str(projected_dist),"Had an accuracy of:",str(accu),"had"
      "an average accuracy of:",str(avg))
