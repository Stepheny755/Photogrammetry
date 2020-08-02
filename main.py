import cv2
import numpy as np
from PIL import Image,ExifTags
import skimage.exposure as skie

from image_utils import image_utils

if(__name__=="__main__"):
    iu = image_utils()

    raw_path = "data\drive-download-20200716T225425Z-001"
    jpg_path = "data\photos1"
    workspace_path = "data\workspace1v2"

    print(iu.read_raws(raw_path))
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
