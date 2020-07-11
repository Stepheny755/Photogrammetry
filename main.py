import cv2, numpy as np
from PIL import Image,ExifTags
import Process

def save_frames(video_name,path):
    vidcap = cv2.VideoCapture(path+video_name)
    bgs = cv2.createBackgroundSubtractorMOG()
    success,image = vidcap.read()
    frame = 0
    while success:
        image = rotate_image(image,270)
        cv2.imwrite(path+("frame%d.jpg"%frame),rotated_img)
        success,image = vidcap.read()
        frame+=1
        print("Saved frame "+str(frame))



if(__name__=="__init__"):
    img = cv2.imread('F:\res\photos3_20200710_224834.jpg')
    bgs = cv2.createBackgroundSubtractorMOG()
    fgmask = bgs.apply(img)
    cv2.imwrite("test",fgmask)
