import cv2, numpy as np
from PIL import Image,ExifTags
import image_utils

if(__name__=="__init__"):
    img = cv2.imread('F:\res\photos3_20200710_224834.jpg')
    bgs = cv2.createBackgroundSubtractorMOG()
    fgmask = bgs.apply(img)
    cv2.imwrite("test",fgmask)
