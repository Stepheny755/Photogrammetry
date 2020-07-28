import cv2, numpy as np
from PIL import Image,ExifTags
from process import Process
import skimage.exposure as skie

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
