from image_utils import image_utils
from pytesseract import Output
import os,cv2,pyautogui,pytesseract
import numpy as np

class reconstruction():

    def __init__(self):
        self.width,self.height = pyautogui.size()
        self.utils = image_utils()
        self.resources_path = "resources\\"
        self.resources_ext = ".png"

    def get_screenshot(self):
        img = self.utils.print_screen(None)
        return img

    def get_ocr_data(self,img):
        img = self.utils.cv2_to_pil(img)
        return pytesseract.image_to_data(img,output_type=Output.DICT)

    def get_bound_boxes(self,img,template_name):
        template = cv2.imread(self.resources_path+template_name+self.resources_ext)
        #cv2.imshow('template',template)
        #cv2.waitKey(0)
        return self.get_bound_boxes_tpm(img,template)

    def get_bound_boxes_tpm(self,img,template,threshold=0.8):
        print(template.shape)
        c,w,h = template.shape[::-1]
        res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        pred_confidence = 0
        x=0
        y=0
        for pt in zip(*loc[::-1]):
            if(res[pt[::-1]]>=pred_confidence):
                pred_confidence=res[pt[::-1]]
                print(pt)
                x = pt[0]
                y = pt[1]
        return x,y,w,h

    def draw_bound_boxes(self,img,x,y,w,h):
        cv2.rectangle(img,(x,y),(x+w,y+h), (0,0,255), 2)
        cv2.imshow('img',img)
        cv2.waitKey(0)

    def get_center(self,x,y,w,h):
        return (2*x+w)/2,(2*y+h)/2

    #def

if(__name__=="__main__"):
    r = reconstruction()
    img = r.get_screenshot()
    coords = r.get_bound_boxes(img,'reconstruction')
    #r.draw_bound_boxes(img,*coords)
    #print(r.get_center(*coords))
    #pyautogui.moveTo(r.get_center(*coords))
