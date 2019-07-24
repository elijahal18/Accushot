import cv2
import imutils
import argparse
#import all necissary image processing imports and pins for raspberry pi


def imageprocessing(getvid):
    ap = argparse.ArgumentParser()
    ap.add_argument(getvid, "--video", required=True,
        help="get vid")#add argument for video
    args = vars(ap.parse_args())

    redupper=(20,90,50)#found by messing with http://colorizer.org/
    redlower=(0,55,25)#these are also hfv

    #Set up argument to grab video data
    vs = cv2.VideoCapture(args["video"])
    time.sleep(2.0)
    coordlst=[]#again do we want to do this as a list or have a deque and then put it in a list

    while True:
        frame=vs.read()#read frame by frame

        frame = imutils.resize(frame, width=600)#probably dont want to resize
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)#make it easier to process

        mask = cv2.inRange(hsv, redLower, redUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        #create a way to easily and quickly find red and remove any errors

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)#make sure works for all versions of cv
        cnts = imutils.grab_contours(cnts)

        center=None#initialize the center
        
        if len(cnts) > 0:
                    # find the largest contour in the mask, then use
                    # it to compute the minimum enclosing circle and
                    # centroid
            c = max(cnts, key=cv2.contourArea)#largest contour area
            ((x, y), radius) = cv2.minEnclosingCircle(c)#initialize location of smallest circle that can completly fit over object
            M = cv2.moments(c)#places this in a moment dictionary for xy
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))#centroidx=(M10/M00) centroidy=M1/M0
        coordlst.append(center)#put that in as a list item
        if coordlst[len(coordlst)-1][0]>=1.05*(coordlst[len(coordlst)-5][0]:
            break

    vs.release()

    cv2.destroyAllWindows()

    return coordlst

def target_location(getvid):
    ap = argparse.ArgumentParser()
    ap.add_argument(getvid, "--video", required=True,
        help="get vid")#add argument for video
    args = vars(ap.parse_args())

    greenupper=(20,90,50)#found by messing with http://colorizer.org/
    greenlower=(0,55,25)#these are also hfv

    vs = cv2.VideoCapture(args["video"])
    time.sleep(2.0)

    frame=vs.read()
    frame = imutils.resize(frame, width=600)#probably dont want to resize
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)#make sure works for all versions of cv
    cnts = imutils.grab_contours(cnts)
    center=None#initialize the center
        
    if len(cnts) > 0:
                    # find the largest contour in the mask, then use
                    # it to compute the minimum enclosing circle and
                    # centroid
        c = max(cnts, key=cv2.contourArea)#largest contour area
        ((x, y), radius) = cv2.minEnclosingCircle(c)#initialize location of smallest circle that can completly fit over object
        M = cv2.moments(c)#places this in a moment dictionary for xy
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))#centroidx=(M10/M00) centroidy=M1/M0
    vs.release()

    cv2.destroyAllWindows()
    return center
    
class StopWatch:#might want to put this in another function
    def __init__(self):
        pass

    def start(self):
        """Starts the timer"""
        self.start = datetime.datetime.now()
        return self.start

    def stop(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return message + str(self.stop - self.start)



