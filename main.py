import cv2, numpy as np
from PIL import Image,ExifTags
from process import Process
import skimage.exposure as skie

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

def load_images(path):
    files = list([os.path.join(folder, f) for f in os.listdir(folder)])


if(__name__=="__main__"):
    #path  = ".\data\photos1"




'''
    print("here")
    img = cv2.imread("1.jpg")
    print("image read")
    print(img)
    bgs = cv2.createBackgroundSubtractorMOG2()
    fgmask = bgs.apply(img)
    cv2.imwrite("test.jpg",fgmask)
    print("image saved")
'''
