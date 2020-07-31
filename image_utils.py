import cv2
import os
import numpy as np
import rawpy
from PIL import Image,ImageGrab,ExifTags

class image_utils():

    def save_frames(self,video_name,path):
        vidcap = cv2.VideoCapture(path+video_name)

        success,image = vidcap.read()
        frame = 0
        while success:
            #image = rotate_image(image,270)
            os.mkdir()
            cv2.imwrite(path+("frame%d.jpg"%frame),rotated_img)
            success,image = vidcap.read()
            frame+=1
            print("Saved frame "+str(frame))

    def cv2_to_pil(self,image):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        return Image.fromarray(image)

    def pil_to_cv2(self,image):
        image_arr = np.array(image)
        return cv2.cvtColor(image_arr,cv2.COLOR_RGB2BGR)

    def rotate_image(self,image,angle):
        rows,cols = image.shape[:2]
        M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1.0)
        return cv2.warpAffine(image,M,(cols,rows))

    def rotate_image(self,image,angle,center):
        rows,cols = image.shape[:2]
        M = cv2.getRotationMatrix2D(center,angle,1.0)
        return cv2.warpAffine(image,M,(cols,rows))

    def print_screen(self,bounding):
        img = ImageGrab.grab(bbox=bounding)
        img = self.pil_to_cv2(img)
        return img

    def list_images(self,path):
        image_names = list([os.path.join(path, f) for f in os.listdir(path)])
        return image_names

    def read_images(self,path):
        image_names = self.list_images(path)

    def read_raws(self,path):
        image_names = self.list_images(path)
        raws = list([rawpy.imread(image_names) for f in os.listdir(path)])
        return raws
